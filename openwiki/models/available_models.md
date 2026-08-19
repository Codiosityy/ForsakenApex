
*   Title: `# Model Files`
*   Project Name: `Forsaken Apex`
*   Directory: `/models`
*   Content Summary: 22 checkpoint files, ~69MB each, total ~1.5GB.
*   Specific Files:
    *   `restoration_best.pt`: Main checkpoint for inference, contains `state_dict`.
    *   `final_model_weights_only.pt`: Weights only, no optimizer state.
    *   `base_restoration_best.pt`: The base model.
    *   `epoch_001.pt` through `epoch_020.pt`: Epoch-specific checkpoints.
*   Format: Markdown wiki page.

    *   A good wiki page needs structure:
        *   Introduction/Overview.
        *   Directory Structure/Summary.
        *   File Descriptions (Detailed).
        *   Usage/Technical Notes (Inference vs. Training).
        *   Storage Information.

    *   *Title:* `# Model Files`

    *   *Introduction:* Mention that this page documents the model assets for the Forsaken Apex project.

    *   *Directory Overview:*
        *   Path: `/models`
        *   Total Files: 22
        *   Average Size: ~69MB per file
        *   Total Size: ~1.5GB

    *   *File Breakdown (using a table or list for clarity):*

        | Filename | Description | Type |
        | :--- | :--- | :--- |
        | `restoration_best.pt` | **Primary Inference Checkpoint**. Contains the full `state_dict`. | Full Checkpoint |
        | `final_model_weights_only.pt` | Weights only; excludes optimizer state to save space. | Weights Only |
        | `base_restoration_best.pt` | The foundational base model. | Base Model |
        | `epoch_001.pt` - `epoch_020.pt` | Periodic snapshots taken during the training process. | Epoch Checkpoints |

    *   *Detailed Descriptions:*
        *   *restoration_best.pt:* Emphasize this is what users/developers should use for inference.
        *   *final_model_weights_only.pt:* Explain *why* it exists (smaller footprint, no optimizer).
        *   *Epoch files:* Explain their purpose (resuming training, monitoring progress).

    *   *Usage Notes:*
        *   How to load `restoration_best.pt`.
        *   Note on the difference between weights-only and full checkpoints.

    *   Check against requirements:
        *   Title correct? Yes.
        *   Project name included? Yes.
        *   22 files/69MB/1.5GB mentioned? Yes.
        *   `restoration_best.pt` (inference/state_dict) mentioned? Yes.
        *   `final_model_weights_only.pt` (weights only) mentioned? Yes.
        *   `base_restoration_best.pt` mentioned? Yes.
        *   `epoch_001` to `epoch_020` mentioned? Yes.

    *   Use bolding for emphasis.
    *   Use code blocks for file names.
    *   Use a table for the file list to make it "wiki-style" and professional.
