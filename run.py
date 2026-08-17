import os
import sys
import glob
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F


# ─── Model Architecture ───────────────────────────────────────────────────────

class DenseBlock(nn.Module):
    def __init__(self, nf=64, gc=32):
        super().__init__()
        self.c1 = nn.Conv2d(nf, gc, 3, 1, 1)
        self.c2 = nn.Conv2d(nf + gc, gc, 3, 1, 1)
        self.c3 = nn.Conv2d(nf + 2*gc, gc, 3, 1, 1)
        self.c4 = nn.Conv2d(nf + 3*gc, gc, 3, 1, 1)
        self.c5 = nn.Conv2d(nf + 4*gc, nf, 3, 1, 1)
        self.act = nn.LeakyReLU(0.2, inplace=True)

    def forward(self, x):
        x1 = self.act(self.c1(x))
        x2 = self.act(self.c2(torch.cat([x, x1], 1)))
        x3 = self.act(self.c3(torch.cat([x, x1, x2], 1)))
        x4 = self.act(self.c4(torch.cat([x, x1, x2, x3], 1)))
        x5 = self.c5(torch.cat([x, x1, x2, x3, x4], 1))
        return x + 0.2 * x5


class RRDB(nn.Module):
    def __init__(self, nf=64, gc=32):
        super().__init__()
        self.blocks = nn.Sequential(DenseBlock(nf, gc), DenseBlock(nf, gc), DenseBlock(nf, gc))

    def forward(self, x):
        return x + 0.2 * self.blocks(x)


class PixelShuffleUpsample(nn.Module):
    def __init__(self, nf, scale):
        super().__init__()
        layers, s = [], scale
        while s > 1:
            layers += [nn.Conv2d(nf, nf * 4, 3, 1, 1), nn.PixelShuffle(2), nn.LeakyReLU(0.2, inplace=True)]
            s //= 2
        self.net = nn.Sequential(*layers) if layers else nn.Identity()

    def forward(self, x):
        return self.net(x)


class RestorationNet(nn.Module):
    def __init__(self, in_ch=1, out_ch=1, nf=64, gc=32, n_rrdb=8, scale=2):
        super().__init__()
        self.scale = scale
        self.head = nn.Conv2d(in_ch, nf, 3, 1, 1)
        self.body = nn.Sequential(*[RRDB(nf, gc) for _ in range(n_rrdb)])
        self.body_tail = nn.Conv2d(nf, nf, 3, 1, 1)
        self.noise_head = nn.Sequential(
            nn.Conv2d(nf, nf // 2, 3, 1, 1), nn.LeakyReLU(0.2, inplace=True), nn.Conv2d(nf // 2, in_ch, 3, 1, 1))
        self.upsample = PixelShuffleUpsample(nf, scale)
        self.hr_conv = nn.Conv2d(nf, nf, 3, 1, 1)
        self.act = nn.LeakyReLU(0.2, inplace=True)
        self.out_conv = nn.Conv2d(nf, out_ch, 3, 1, 1)

    def forward(self, lr):
        feat0 = self.head(lr)
        feat = self.body_tail(self.body(feat0)) + feat0
        _ = self.noise_head(feat)
        up = self.act(self.hr_conv(self.upsample(feat)))
        residual = self.out_conv(up)
        bicubic = F.interpolate(lr, scale_factor=self.scale, mode="bicubic", align_corners=False)
        restored = torch.clamp(bicubic + residual, 0.0, 1.0)
        return restored


# ─── Inference ────────────────────────────────────────────────────────────────

def load_npy(path):
    arr = np.load(path).astype(np.float32)
    if arr.max() > 2.0:
        arr /= 255.0
    t = torch.from_numpy(arr)
    if t.ndim == 2:
        t = t.unsqueeze(0)
    elif t.ndim == 3 and t.shape[-1] in (1, 3):
        t = t.permute(2, 0, 1)
    return t.unsqueeze(0)


def main():
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <input-dir> <output-dir>")
        sys.exit(1)

    input_dir = sys.argv[1]
    output_dir = sys.argv[2]
    os.makedirs(output_dir, exist_ok=True)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    net = RestorationNet(scale=2).to(device)

    ckpt_path = os.path.join(os.path.dirname(__file__), "models", "restoration_best.pt")
    if not os.path.isfile(ckpt_path):
        print(f"Error: checkpoint not found at {ckpt_path}")
        sys.exit(1)

    ckpt = torch.load(ckpt_path, map_location=device)
    net.load_state_dict(ckpt["model"])
    net.eval()

    input_files = sorted(glob.glob(os.path.join(input_dir, "*.npy")))
    if not input_files:
        print(f"No .npy files found in {input_dir}")
        sys.exit(1)

    print(f"Found {len(input_files)} images in {input_dir}")

    nan_count = 0
    with torch.no_grad():
        for fp in input_files:
            lr = load_npy(fp).to(device)
            restored = net(lr)
            out = restored.squeeze().cpu().numpy()
            bad = np.isnan(out) | np.isinf(out)
            if bad.any():
                nan_count += 1
                print(f"  WARNING: {os.path.basename(fp)} — {bad.sum()} NaN/Inf values detected (clamping)")
            out = np.nan_to_num(out, nan=0.0, posinf=1.0, neginf=0.0)
            out = np.clip(out, 0.0, 1.0).astype(np.float32)
            out_path = os.path.join(output_dir, os.path.basename(fp))
            np.save(out_path, out)

    if nan_count:
        print(f"WARNING: {nan_count}/{len(input_files)} images had NaN/Inf — possible fp16 overflow in checkpoint")
    print(f"Saved {len(input_files)} restored images to {output_dir}")


if __name__ == "__main__":
    main()
