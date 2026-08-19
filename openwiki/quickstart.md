
*   Title: `# Quick Start Guide`
*   Project Name: `Forsaken Apex` (KLA 2026 image restoration project)
*   Sections required:
    1.  Project Overview (competition entry for image restoration).
    2.  Prerequisites (Python 3.8+, NVIDIA GPU, CUDA).
    3.  Installation (`pip install -r requirements.txt`).
    4.  Running Inference (`python run.py input_dir output_dir`).
    5.  Input Format (`.npy` files with grayscale images).
    6.  Output Format (`.npy` + `.png` files).
    7.  Performance (PSNR 28.47dB, SSIM 0.767, LPIPS 0.164).
*   Additional requirement: Navigation links to other wiki pages.
*   Format: Markdown.

    *   *Title:* `# Quick Start Guide`

    *   *Navigation (Top):* Needs links like `[Project Overview](#)`, `[Installation](#)`, `[Troubleshooting](#)`, etc. Since the user didn't specify the names of other pages, I'll use placeholders like `[Installation Guide](installation.md)`, `[Model Architecture](architecture.md)`, and `[Troubleshooting](troubleshooting.md)`.

    *   *Section 1: Project Overview:*
        *   Heading: `## Project Overview`
        *   Content: "Forsaken Apex" is a competition entry for the KLA 2026 image restoration challenge. It focuses on advanced restoration techniques to recover high-fidelity images from degraded inputs.

    *   *Section 2: Prerequisites:*
        *   Heading: `## Prerequisites`
        *   Content:
            *   Python 3.8 or higher.
            *   NVIDIA GPU (for hardware acceleration).
            *   CUDA Toolkit (compatible with your GPU).

    *   *Section 3: Installation:*
        *   Heading: `## Installation`
        *   Content:
            1. Clone the repository.
            2. Create a virtual environment (optional but recommended).
            3. Run: `pip install -r requirements.txt`

    *   *Section 4: Running Inference:*
        *   Heading: `## Running Inference`
        *   Content: Use the provided script to process directories.
        *   Command: `python run.py <input_dir> <output_dir>`

    *   *Section 5: Input Format:*
        *   Heading: `## Input Format`
        *   Content: The model expects `.npy` files containing grayscale image data.

    *   *Section 6: Output Format:*
        *   Heading: `## Output Format`
        *   Content: For every input file, the system generates:
            *   `.npy` file (raw restored data).
            *   `.png` file (visual representation).

    *   *Section 7: Performance:*
        *   Heading: `## Performance Metrics`
        *   Content (Table format is best for metrics):
            | Metric | Value |
            | :--- | :--- |
            | PSNR | 28.47 dB |
            | SSIM | 0.767 |
            | LPIPS | 0.164 |

    *   Check against all user requirements.
    *   Ensure Markdown syntax is correct (headers, code blocks, lists, tables).
    *   Add a "Navigation" section at the top.

(This matches the provided good response).
