
*   Title: `# Development Setup`
*   Project Name: `Forsaken Apex`
*   Content Requirements:
    *   `requirements.txt` details: `torch`, `torchvision`, `numpy`, `torchmetrics`, `lpips`.
    *   System Requirements: Python 3.8+, NVIDIA GPU with CUDA.
    *   Installation command: `pip install -r requirements.txt`.
    *   Inference command: `python run.py <input-dir> <output-dir>`.
    *   Development workflow: Jupyter Notebook (`Untitled1(3).ipynb`) for training experiments.
    *   Storage: Model checkpoints are saved to the `/models` directory.
*   Format: Markdown wiki page.

    *   *Heading:* `# Development Setup`
    *   *Introduction:* Brief mention of the project (Forsaken Apex).
    *   *System Requirements Section:* Python version and Hardware (GPU/CUDA).
    *   *Installation Section:* The `pip` command and a breakdown of dependencies.
    *   *Usage Section:* How to run inference.
    *   *Development Workflow Section:* Jupyter notebooks and where files are saved.

    *   *Title:* `# Development Setup`

    *   *System Requirements:*
        *   Python: 3.8 or higher.
        *   Hardware: NVIDIA GPU (required for CUDA support).

    *   *Installation:*
        *   Command: `pip install -r requirements.txt`
        *   Dependency breakdown (use a list or table for clarity):
            *   `torch`: Core PyTorch library.
            *   `torchvision`: Computer vision utilities.
            *   `numpy`: Numerical computing.
            *   `torchmetrics`: Metrics for evaluating models.
            *   `lpips`: Learned Perceptual Image Patch Similarity.

    *   *Running Inference:*
        *   Command: `python run.py <input-dir> <output-dir>`
        *   Explanation: `<input-dir>` is the path to source images, `<output-dir>` is where results go.

    *   *Development Workflow:*
        *   Training: Use Jupyter Notebooks. Specifically, `Untitled1(3).ipynb` is used for experimentation.
        *   Checkpoints: All trained models are saved in the `/models` directory.

    *   Use code blocks (`` ` `` and ` ``` `) for commands and file names.
    *   Use bolding for emphasis.
    *   Use lists for readability.
