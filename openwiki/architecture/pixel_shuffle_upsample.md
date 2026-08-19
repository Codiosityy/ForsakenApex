
*   Role: Technical Writer.
*   Task: Generate a Markdown wiki page.
*   Title: `# PixelShuffleUpsample Module`.
*   Project Context: `Forsaken Apex`.
*   Core Content:
    *   Functionality: Handles arbitrary scale factors by iterating divide-by-2.
    *   Specific implementation for `scale=2`: `Conv2d(nf, nf*4, 3, 1, 1)` $\rightarrow$ `PixelShuffle(2)` $\rightarrow$ `LeakyReLU(0.2)`.
    *   Mathematical/Structural logic: `PixelShuffle` rearranges $(C \cdot r^2, H, W)$ to $(C, H \cdot r, W \cdot r)$.
    *   Edge case: If `scale=1`, uses `Identity`.

    *   Title (H1).
    *   Overview/Description.
    *   Mathematical Formulation/Mechanism.
    *   Implementation Details (Algorithmic logic).
    *   Detailed Architecture (for scale=2).
    *   Edge Cases.
    *   Code Example (optional but highly recommended for a technical wiki).

    *   *Title:* `# PixelShuffleUpsample Module`

    *   *Overview:* This module is part of the `Forsaken Apex` architecture. It's designed for spatial upsampling using the sub-pixel convolution method (PixelShuffle). Unlike standard interpolation, this learns the upscaling parameters.

    *   *Mechanism (The math):* I need to explain the reshaping.
        Input shape: $(C \cdot r^2, H, W)$
        Output shape: $(C, H \cdot r, W \cdot r)$
        Where $r$ is the upscale factor.

    *   *Scaling Logic:* The user specified "handles arbitrary scale factors by iterating divide-by-2". This means if the user wants scale=4, the module applies the scale=2 block twice.
        *   Scale 1: Identity.
        *   Scale 2: Conv $\rightarrow$ Shuffle $\rightarrow$ LeakyReLU.
        *   Scale 4: (Conv $\rightarrow$ Shuffle $\rightarrow$ LeakyReLU) $\times 2$.

    *   *Architecture (Scale 2 detail):*
        1.  `Conv2d`: `in_channels=nf`, `out_channels=nf * 4`, `kernel_size=3`, `stride=1`, `padding=1`.
        2.  `PixelShuffle`: `upscale_factor=2`.
        3.  `LeakyReLU`: `negative_slope=0.2`.

    *   *Tone:* Formal, precise, technical.
    *   *Formatting:* Use LaTeX for math, code blocks for logic, and bold text for emphasis.

    *   *Correction:* I should clarify that $nf$ represents the number of input feature channels.
    *   *Addition:* A "Complexity/Note" section adds value to a wiki.

    *   Title: `# PixelShuffleUpsample Module`
    *   Intro: Part of Forsaken Apex.
    *   Mathematical Logic: The tensor reshaping.
    *   Scaling Strategy: Recursive/Iterative approach.
    *   Layer Breakdown: The specific $2\times$ block.
    *   Implementation Summary table.
