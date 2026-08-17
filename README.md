# AI-Based Restoration of Degraded Images — Forsaken Apex

RRDB-based single-image restoration network (5.997M parameters) that upscales and denoises degraded grayscale inputs by 2x.

## Setup

```bash
pip install -r requirements.txt
```

Place the trained checkpoint at:

```
models/restoration_best.pt
```

## Usage

```bash
python run.py <input-dir> <output-dir>
```

- `<input-dir>` — directory containing `.npy` degraded images (grayscale, float `[0,1]` or uint8 `[0,255]`)
- `<output-dir>` — directory where restored `.npy` files are written

Output images are saved as float32 `.npy` files with values in `[0, 1]`, shape `(H, W)` where `H = 2 * input_h` and `W = 2 * input_w`.

## Model

| Component | Detail |
|-----------|--------|
| Architecture | RestorationNet (RRDB × 8, PixelShuffle 2x) |
| Parameters | 5.997M |
| Input | 1-channel grayscale, arbitrary spatial size |
| Output | 1-channel grayscale, 2× input resolution |
| Scale | 2× (bicubic residual learning) |

### Architecture breakdown

- **Head:** `Conv2d(1, 64)` — extract initial features
- **Body:** 8 × RRDB blocks (each RRDB = 3 × DenseBlock with dense concatenation)
- **Upsample:** PixelShuffle 2× via `Conv2d(64, 256) → PixelShuffle(2)`
- **Output:** Global residual on bicubic interpolation — `clamp(bicubic + conv(features), 0, 1)`

## Training details

- **Loss:** Composite — Charbonnier + Gradient + Physics Consistency + SSIM + LPIPS + Blind Spot
- **Optimizer:** AdamW (lr=2e-4, weight_decay=1e-4)
- **Scheduler:** CosineAnnealingLR (T_max=100)
- **Batch size:** 16 effective (4 × 4 gradient accumulation)
- **Mixed precision:** AMP with GradScaler
- **Epochs:** 100 base + 15 refinement
- **Best metrics:** PSNR 26.81 dB, SSIM 0.771, LPIPS 0.181

## Environment

- Python ≥ 3.10
- CUDA-capable GPU (NVIDIA, tested with CUDA 12.x)
- No internet access required at inference time
