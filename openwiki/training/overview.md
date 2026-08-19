
*   Title: `# Training Overview`
*   Project Name: `Forsaken Apex` (KLA 2026 image restoration project).
*   Training Strategy Details:
    *   Loss Function: Composite (L1 pixel loss + SSIM loss + LPIPS perceptual loss).
    *   Optimizer: AdamW (lr=2e-4, betas=(0.9, 0.999), weight_decay=1e-4).
    *   Scheduler: CosineAnnealingLR.
    *   Batch Size: 8.
    *   Precision: Mixed precision (AMP).
    *   Reproducibility: Random seed 42.
*   Data Details:
    *   Composition: 50% real low/high pairs + 50% synthetic degradation (speckle noise + Gaussian readout noise).
*   Visual Element: Mermaid diagram showing the training pipeline.
*   Format: Markdown wiki page.

    *   Title.
    *   Introduction (briefly mention the project context).
    *   Training Strategy (Optimizer, Scheduler, Precision, Reproducibility).
    *   Loss Function (The composite approach).
    *   Data Composition (Real vs. Synthetic).
    *   Training Pipeline (Mermaid diagram).

    *   *Title:* `# Training Overview`

    *   *Introduction:* This page outlines the training methodology for the **Forsaken Apex** image restoration project, part of the KLA 2026 initiative.

    *   *Training Strategy Section:*
        *   Use a table or a list for clarity.
        *   Optimizer: AdamW ($\eta=2 \times 10^{-4}$, $\beta=(0.9, 0.999)$, $\lambda=1 \times 10^{-4}$).
        *   Scheduler: CosineAnnealingLR.
        *   Batch Size: 8.
        *   Precision: Automatic Mixed Precision (AMP).
        *   Reproducibility: Seed 42.

    *   *Loss Function Section:*
        *   Explain the "Composite Loss" concept.
        *   $L_{total} = \alpha L_1 + \beta L_{SSIM} + \gamma L_{LPIPS}$. (I'll list them clearly).
        *   L1: Pixel-wise accuracy.
        *   SSIM: Structural similarity.
        *   LPIPS: Perceptual quality.

    *   *Data Composition Section:*
        *   50% Real-world pairs (Ground truth matched).
        *   50% Synthetic (Speckle + Gaussian readout noise).

    *   *Mermaid Diagram:*
        *   Flow: Input Data $\rightarrow$ Augmentation/Degradation $\rightarrow$ Model $\rightarrow$ Output $\rightarrow$ Loss Calculation $\rightarrow$ Optimizer $\rightarrow$ Update Weights.

    *   *Mermaid Logic:*
        ```mermaid
        graph TD
          A[Dataset] --> B{Data Split}
          B -->|50%| C[Real Low/High Pairs]
          B -->|50%| D[Synthetic Degradation]
          D -->|Speckle + Gaussian| E[Synthetic Low-Res]
          C --> F[Model Training]
          E --> F
          F --> G[Output Image]
          G --> H[Composite Loss Calculation]
          H -->|L1 + SSIM + LPIPS| I[Optimizer: AdamW]
          I --> J[Weights Update]
          J --> F
        ```

    *   Check against all constraints:
        *   Title correct? Yes.
        *   Project name included? Yes.
        *   Losses included? Yes.
        *   AdamW params correct? Yes.
        *   Scheduler/Batch/AMP/Seed included? Yes.
        *   Data split/noise types included? Yes.
        *   Mermaid diagram included? Yes.
