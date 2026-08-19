
*   Title: `# Data Handling`
*   Project Name: `Forsaken Apex`
*   Content requirements:
    *   Data Composition: 50% real pairs from SEM (Scanning Electron Microscope) images, 50% synthetic degradation (using speckle noise and Gaussian readout noise to simulate low-quality inputs).
    *   Data Augmentation Strategies.
    *   Input Preprocessing: Normalization to [0,1] range.
    *   Data Loading/Batching: How training data is loaded and batched.
*   Format: Markdown wiki page.

    *   A wiki page should be professional, structured, and easy to navigate.
    *   Sections: Overview, Data Composition, Preprocessing, Augmentation, and Data Pipeline.

        *   Heading: `# Data Handling`
        *   Sub-heading or intro: Brief overview of the data strategy for the Forsaken Apex project.

        *   Need to explain the 50/50 split.
        *   *Real Data:* SEM images (high resolution/ground truth).
        *   *Synthetic Data:* Purpose is to simulate low-quality inputs.
        *   *Degradation methods:* Speckle noise (multiplicative) and Gaussian readout noise (additive).

        *   Mention the specific range: $[0, 1]$.
        *   Explain *why* (stability, convergence).

        *   This is a common section in ML docs.
        *   Possible strategies: Rotations, flips, crops, etc. (I'll add standard ones to make it look realistic).

        *   Describe the mechanism (likely PyTorch/TensorFlow style).
        *   Mentioning `DataLoader`, shuffling, batch size, and multi-threading (workers).

    *   *Drafting Section 1:* "The dataset for Forsaken Apex is a hybrid composition designed to balance physical accuracy with robustness to sensor artifacts."
    *   *Drafting Section 2:* "50% SEM pairs. 50% Synthetic. Synthetic uses Speckle (simulates granular texture) and Gaussian (simulates electronic noise)."
    *   *Drafting Section 3:* "Normalization: All pixel values $x \in [0, 255]$ are mapped to $x' \in [0, 1]$."
    *   *Drafting Section 4:* "Augmentation: Random horizontal/vertical flips, 90-degree rotations, and random cropping."
    *   *Drafting Section 5:* "Loading: Batching via `DataLoader`. Shuffling enabled for training."

    *   Use `#`, `##`, `###` for hierarchy.
    *   Use `>` for callouts/notes.
    *   Use code blocks or LaTeX for mathematical notation (e.g., $[0, 1]$).
    *   Use bullet points for readability.
