
*   Role: Technical Writer.
*   Target: Markdown wiki page for the 'Forsaken Apex' project.
*   Title: `# RestorationNet Model`.
*   Topic: Detailed explanation of the `RestorationNet` architecture.
*   Parameters (Constructor): `in_ch=1`, `out_ch=1`, `nf=64`, `gc=32`, `n_rrdb=8`, `scale=2`.
*   Architecture Components:
    *   Head conv.
    *   8 RRDB (Residual-in-Residual Dense Block) bodies.
    *   Body tail conv with a skip connection.
    *   Noise head.
    *   PixelShuffleUpsample.
    *   hr_conv.
    *   out_conv.
*   Forward Pass Logic:
    1.  `feat0 = head(lr)`
    2.  `feat = body_tail(body(feat0)) + feat0`
    3.  `up = act(hr_conv(upsample(feat)))`
    4.  `residual = out_conv(up)`
    5.  `bicubic = F.interpolate(lr, 2x, bicubic)`
    6.  `restored = clamp(bicubic + residual, 0, 1)`
*   Metric: 5.997M parameters.
*   Requirement: Include full code.

    *   Title: `# RestorationNet Model`.
    *   Introduction: Overview of what the model does (image restoration/super-resolution).
    *   Architecture Overview: High-level summary.
    *   Detailed Component Breakdown:
        *   Constructor Parameters.
        *   Layer-by-layer explanation.
    *   Mathematical/Operational Flow (The Forward Pass).
    *   Model Complexity (Parameters).
    *   Implementation (Code Block).

    *   *Introduction*: RestorationNet is a deep learning architecture designed for image restoration tasks within the Forsaken Apex project. It utilizes a residual learning framework to reconstruct high-resolution details from low-resolution inputs.

    *   *Parameters*:
        *   `in_ch`: Input channels (1 for grayscale).
        *   `out_ch`: Output channels (1).
        *   `nf`: Number of feature maps (64).
        *   `gc`: Growth channel/Group channel (32).
        *   `n_rrdb`: Number of RRDB blocks (8).
        *   `scale`: Upscaling factor (2).

    *   *Architecture Breakdown*:
        *   *Head Conv*: Initial feature extraction.
        *   *RRDB Body*: The core processing engine, consisting of 8 Residual-in-Residual Dense Blocks.
        *   *Body Tail*: A convolution layer followed by a long skip connection from the head.
        *   *Upsampling*: Uses `PixelShuffleUpsample` to increase spatial resolution.
        *   *HR Conv & Out Conv*: Refinement layers.
        *   *Residual Learning*: The model learns the *difference* between a bicubic upscaled image and the ground truth, rather than the whole image.

    *   *Forward Pass Logic (Mathematical notation)*:
        *   $F_0 = \text{Head}(LR)$
        *   $F_{body} = \text{Body}(F_0)$
        *   $F_{tail} = \text{Tail}(F_{body}) + F_0$
        *   $U = \text{Activation}(\text{HR\_Conv}(\text{Upsample}(F_{tail})))$
        *   $R = \text{Out\_Conv}(U)$
        *   $B = \text{Bicubic}(LR)$
        *   $\text{Output} = \text{Clamp}(B + R, 0, 1)$

    *   *Code implementation*: Needs to be a complete, runnable PyTorch class.
        *   Need `RRDB` and `ResidualDenseBlock` (implied by RRDB).
        *   Need `PixelShuffleUpsample`.
        *   Need the main `RestorationNet` class.

    *   *Self-Correction during coding*: The prompt specifies `body_tail(body(feat0)) + feat0`. This means the `body` is a sequence of 8 RRDBs, and `body_tail` is a single convolution.
    *   *Wait*, the prompt says `noise_head` is a component. I should include a placeholder or a functional implementation of it in the code to satisfy the requirement.
    *   *Complexity Check*: 5.997M params. I'll ensure the architecture structure matches the description so the parameter count is realistic.

    *   Use bolding for parameters.
    *   Use LaTeX for math.
    *   Use clear headings.
    *   Ensure the code is well-commented.
