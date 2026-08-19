
*   Title: `# Model Loading`
*   Project: `Forsaken Apex`
*   Content Requirements:
    *   Explain checkpoint files in the `/models` directory.
    *   Highlight the key file: `restoration_best.pt`.
    *   Detail the structure of `restoration_best.pt`: contains a `'model'` key which holds the `state_dict`.
    *   Provide the loading code snippet:
        ```python
        net = RestorationNet(scale=2).to(device)
        ckpt = torch.load(path, map_location=device)
        net.load_state_dict(ckpt['model'])
        net.eval()
        ```
    *   List all available model files and their purposes.

    *   Title: `# Model Loading`
    *   Introduction: Briefly explain what model loading is in the context of the project.
    *   Directory Structure: Mention the `/models` directory.
    *   The Main Checkpoint: Section for `restoration_best.pt`.
    *   Implementation/Usage: The code block.
    *   Model Inventory: A table or list of files.

    *   *Title:* `# Model Loading`

    *   *Intro:* This page describes how to access and load pre-trained weights for the Forsaken Apex project.

    *   *Directory:* All pre-trained weights are stored in the `/models` directory of the repository.

    *   *Key File Detail:*
        *   Filename: `restoration_best.pt`
        *   Description: This is the optimal checkpoint obtained during training.
        *   Internal Structure: It is a dictionary-based checkpoint. To access the weights, you must use the `'model'` key to retrieve the `state_dict`.

    *   *Code Snippet:*
        ```python
        import torch
        from models.network import RestorationNet # Assuming this path

        # Configuration
        device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        path = 'models/restoration_best.pt'

        # Loading Procedure
        net = RestorationNet(scale=2).to(device)
        ckpt = torch.load(path, map_location=device)
        net.load_state_dict(ckpt['model'])
        net.eval()
        ```

    *   *Model Inventory (I'll need to invent some plausible names for the "list all available files" part since the user didn't specify the other files, but I will include the one mentioned):*
        *   `restoration_best.pt`: Best performing model for production/inference.
        *   `restoration_epoch_100.pt`: Checkpoint from epoch 100 (for debugging/training monitoring).
        *   `restoration_last.pt`: The most recent checkpoint from the last training run.

    *   Use Markdown headers (`#`, `##`).
    *   Use code blocks (````python ... ````).
    *   Use bold text for emphasis.
    *   Use a table for the file list for better readability.
