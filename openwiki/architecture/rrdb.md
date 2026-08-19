
*   Role: Technical Writer.
*   Format: Markdown wiki page.
*   Title: `# RRDB (Residual in Residual Dense Block)`.
*   Project Context: `Forsaken Apex`.
*   Key Technical Content:
    *   Structure: Stacks 3 `DenseBlocks` using `nn.Sequential`.
    *   Mechanism: Outer residual connection with 0.2 scaling.
    *   Forward Pass logic: `return x + 0.2 * blocks(x)`.
    *   Purpose/Benefit: Creates a deep residual learning framework that prevents training instability.

    *   Standard wiki structure: Title, Overview, Architecture, Implementation Details (Math/Code logic), and Benefits/Conclusion.

    *   *Header:* `# RRDB (Residual in Residual Dense Block)`
    *   *Project Context:* Mention it's part of the `Forsaken Apex` architecture.

    *   *Overview:* Define what RRDB is. It's a sophisticated block used in super-resolution or deep feature extraction tasks to allow for very deep networks without vanishing gradients.

    *   *Architecture:*
        *   Internal component: `DenseBlock`.
        *   Stacking method: `nn.Sequential` (PyTorch context implied).
        *   Number of blocks: 3.
        *   Residual type: "Residual in Residual" (meaning a residual connection wraps around a set of residual blocks).

    *   *Mathematical/Logic Detail:*
        *   Input: $x$
        *   Transformation: $F(x) = \text{DenseBlock}_3(\text{DenseBlock}_2(\text{DenseBlock}_1(x)))$
        *   Output: $y = x + 0.2 \cdot F(x)$
        *   Highlight the $0.2$ scaling factor.

    *   *Benefits:*
        *   Deep residual learning framework.
        *   Prevents training instability (gradient vanishing/exploding).
        *   Allows for higher capacity without losing signal integrity.

    *   *Tone Check:* Professional, technical, concise, and clear.
    *   *Formatting:* Use bolding, LaTeX for math, and code blocks for clarity.

    *   *Title:* `# RRDB (Residual in Residual Dense Block)`
    *   *Introduction:* Part of the `Forsaken Apex` model architecture.
    *   *Structure Section:* Explain the 3-block stack.
    *   *The Residual Mechanism:* Explain the $0.2$ scaling.
    *   *Implementation:* Show the pseudo-code/logic.
    *   *Conclusion:* Why we use it.
