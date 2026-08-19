
*   Title: `# Inference Guide`
*   Project: `Forsaken Apex`
*   Command: `python run.py <input-dir> <output-dir>`
*   Input format: `.npy` files containing grayscale images.
*   Output format: `.npy` + `.png` files.
*   Model Details:
    *   Checkpoint: `restoration_best.pt`
    *   Architecture: `RestorationNet`
    *   Method: Bicubic residual learning.
*   Processing logic:
    *   Handles NaN/Inf detection (with warnings).
    *   Clips output to range $[0, 1]$.
*   Requirements: PyTorch, CUDA GPU.
*   Environment: Works offline (no internet required).
*   Format: Markdown wiki page.

    A good technical wiki page should have:
    *   Title
    *   Overview/Introduction
    *   Prerequisites/Requirements
    *   Usage/Command Syntax
    *   Input/Output Specifications
    *   Technical Details (Model/Process)
    *   Troubleshooting/Notes

    *   *Title:* `# Inference Guide`

    *   *Introduction:* Briefly describe what this guide is for. "This guide provides instructions on how to perform inference using the Forsaken Apex restoration model."

    *   *Prerequisites:*
        *   PyTorch installed.
        *   CUDA-enabled GPU (crucial for performance/requirement).
        *   Mention it works offline.

    *   *Usage:*
        *   Show the command: `python run.py <input-dir> <output-dir>`
        *   Explain the placeholders.

    *   *Input/Output:*
        *   Input: Folder containing `.npy` files (grayscale).
        *   Output: Folder where `.npy` and `.png` files will be saved.

    *   *Technical Implementation (The "Under the Hood" part):*
        *   Model: `RestorationNet`.
        *   Checkpoint: `restoration_best.pt`.
        *   Core logic: Bicubic residual learning.
        *   Data integrity: NaN/Inf detection + warnings.
        *   Post-processing: Clipping to $[0, 1]$.

    *   *Refining the "Technical Details" section:* Use a list for readability.

    *   Use code blocks for commands.
    *   Use bold text for file names and parameters.
    *   Use LaTeX-style notation or simple text for ranges (e.g., `[0, 1]`).

    *   *Title correct?* Yes.
    *   *Command correct?* Yes.
    *   *Input/Output correct?* Yes.
    *   *Model/Method/Checkpoint included?* Yes.
    *   *NaN/Inf/Clipping included?* Yes.
    *   *Requirements (PyTorch/CUDA/Offline) included?* Yes.
