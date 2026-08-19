
*   Role: Technical Writer.
*   Topic: 'Forsaken Apex' image restoration project (KLA 2026 competition).
*   Page Title: `# Architecture Overview`.
*   Format: Markdown wiki page.
*   Content Requirements:
    1.  System Overview: Mermaid flowchart (LR Input $\rightarrow$ Head Conv $\rightarrow$ 8x RRDB $\rightarrow$ Body Tail Conv $\rightarrow$ skip connection $\rightarrow$ Upsample $\rightarrow$ HR Conv $\rightarrow$ Out Conv $\rightarrow$ (+ bicubic residual) $\rightarrow$ clamp $\rightarrow$ Output).
    2.  DenseBlock details: 5 Conv2d layers ($nf=64, gc=32$), LeakyReLU(0.2), residual scaling 0.2, dense concatenation.
    3.  RRDB details: 3 DenseBlocks, outer residual 0.2.
    4.  PixelShuffleUpsample details: Conv2d + PixelShuffle (2x).
    5.  RestorationNet details: 8 RRDB blocks, bicubic residual learning, noise head, 5.997M params.
    6.  Technical style: Detailed, including code snippets.

    *   *Title:* # Architecture Overview
    *   *Introduction:* Brief context about the Forsaken Apex project for the KLA 2026 competition.

    *   *System Overview Section:*
        *   Text describing the end-to-end pipeline.
        *   Mermaid diagram (Graph TD).
        *   Flow: `LR Input` $\rightarrow$ `Head Conv` $\rightarrow$ `8x RRDB` $\rightarrow$ `Body Tail Conv` $\rightarrow$ `Skip Connection` $\rightarrow$ `Upsample` $\rightarrow$ `HR Conv` $\rightarrow$ `Out Conv` $\rightarrow$ `+ Bicubic Residual` $\rightarrow$ `Clamp` $\rightarrow$ `Output`.

    *   *Component Breakdown:*

        *   *DenseBlock:*
            *   Technical specs: 5 layers, $nf=64$, $gc=32$, LeakyReLU(0.2), scaling=0.2.
            *   Code snippet (PyTorch style).

        *   *RRDB (Residual-in-Residual Dense Block):*
            *   Technical specs: 3 DenseBlocks, outer residual factor 0.2.
            *   Code snippet.

        *   *PixelShuffleUpsample:*
            *   Mechanism: Conv2d followed by PixelShuffle.
            *   Scale: 2x.
            *   Code snippet.

        *   *RestorationNet (The Main Model):*
            *   Architecture: 8 RRDB blocks.
            *   Key feature: Bicubic residual learning (predicting the difference between bicubic upsampling and the ground truth).
            *   Key feature: Noise head (optional/integrated).
            *   Parameter count: 5.997M.
            *   Code snippet (the `forward` pass logic).

    *   *Tone:* Professional, engineering-focused, precise.
    *   *Mathematics/Notation:* Use LaTeX for parameters like $nf=64$.
    *   *Code Style:* Standard PyTorch syntax.

    *   *Mermaid:*
        ```mermaid
        graph TD
            A[LR Input] --> B[Head Conv]
            B --> C[8x RRDB Blocks]
            C --> D[Body Tail Conv]
            D --> E[Skip Connection]
            E --> F[PixelShuffle Upsample]
            F --> G[HR Conv]
            G --> H[Out Conv]
            H --> I[+ Bicubic Residual]
            I --> J[Clamp]
            J --> K[Output]
        ```
        *Wait, the prompt says "skip connection" after Body Tail Conv. Usually, skip connections go from Head Conv to Tail Conv. I will follow the prompt's specific flow: Body Tail Conv $\rightarrow$ skip connection $\rightarrow$ Upsample. This implies a global residual connection or a specific skip from an earlier stage.*

    *   *DenseBlock Details:*
        *   Input channels: $nf$.
        *   Growth rate ($gc$): 32.
        *   Output of each layer: $x_{i+1} = [x_i, \text{conv}(x_i)]$.
        *   Residual scaling: $x = x + 0.2 \cdot \text{dense\_out}$.

    *   *RRDB Details:*
        *   It's a hierarchy. 3 DenseBlocks inside one RRDB.
        *   Outer residual: $x = x + 0.2 \cdot \text{RRDB\_out}$.

    *   *RestorationNet Details:*
        *   Total params: 5.997M.
        *   Residual learning: $y = \text{Model}(x) + \text{Bicubic}(x)$.

    *   Title: # Architecture Overview? Yes.
    *   Mermaid flowchart correct? Yes.
    *   DenseBlock specs correct? Yes.
    *   RRDB specs correct? Yes.
    *   PixelShuffle specs correct? Yes.
    *   RestorationNet specs correct? Yes.
    *   Code snippets included? Yes.
