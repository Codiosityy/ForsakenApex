
*   Title: `# Evaluation Metrics`
*   Project Context: 'Forsaken Apex' KLA 2026 project.
*   Format: Markdown wiki page.
*   Metrics to include:
    1.  PSNR (Peak Signal-to-Noise Ratio)
    2.  SSIM (Structural Similarity Index Measure)
    3.  LPIPS (Learned Perceptual Image Patch Similarity)
    4.  Sharpness
*   Specific requirements for each metric:
    *   Definition/Explanation.
    *   Scale/Range/Unit.
    *   Direction (higher is better/lower is better).
    *   What it indicates about restoration quality.
    *   Formula (where applicable).

    *   *Title:* `# Evaluation Metrics`
    *   *Project Header:* Mention "Forsaken Apex | KLA 2026".

    *   *PSNR:*
        *   Concept: Pixel-level fidelity/error.
        *   Formula: $PSNR = 10 \cdot \log_{10}(\frac{MAX^2}{MSE})$ where $MSE = \frac{1}{mn} \sum \sum [I(i,j) - K(i,j)]^2$.
        *   Unit: dB.
        *   Direction: Higher is better.
        *   Indication: Mathematical reconstruction accuracy.

    *   *SSIM:*
        *   Concept: Perceptual quality (human vision emulation).
        *   Components: Luminance ($l$), Contrast ($c$), Structure ($s$).
        *   Formula: $SSIM(x,y) = [l(x,y)]^\alpha \cdot [c(x,y)]^\beta \cdot [s(x,y)]^\gamma$.
        *   Range: $[0, 1]$ (usually 1 is perfect).
        *   Direction: Higher is better.
        *   Indication: Structural integrity and texture preservation.

    *   *LPIPS:*
        *   Concept: Deep feature similarity (learned perceptual).
        *   Method: Uses deep networks (e.g., VGG) to compare feature maps.
        *   Direction: Lower is better (closer to 0 means more similar).
        *   Indication: Alignment with human perception of "realness" or "naturalness."

    *   *Sharpness:*
        *   Concept: Detail preservation/edge clarity.
        *   Method: Often using Laplacian variance or gradient magnitude.
        *   Indication: Ability to recover lost high-frequency details (avoiding blur).

    *   Use H1 for title.
    *   Use H2 for metric names.
    *   Use LaTeX-style formatting for formulas (using `$$` or `$`).
    *   Use bullet points for readability.
    *   Add a summary table for quick reference (standard wiki practice).

    *   *Drafting PSNR formula:* Need to define MSE first.
    *   *Drafting SSIM formula:* Keep it standard.
    *   *Drafting LPIPS:* Mention VGG as requested.
    *   *Drafting Sharpness:* Since there isn't one "universal" formula like PSNR, I'll use the standard Laplacian Variance approach often used in image processing.

    *   Title correct? Yes.
    *   Project name included? Yes.
    *   All metrics included? Yes.
    *   Direction/Units/Indication included? Yes.
    *   Formulas included? Yes.
