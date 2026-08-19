---
okf_version: "0.1"
---

# Forsaken Apex Wiki

Documentation for the KLA 2026 Image Restoration Competition entry.

## Getting Started

- [Quick Start Guide](quickstart.md) - Project overview, installation, and usage

## Architecture

- [Architecture Overview](architecture/overview.md) - System design and data flow
- [RestorationNet Model](architecture/restoration_net.md) - Main model architecture
- [DenseBlock Module](architecture/dense_block.md) - Dense connectivity block
- [RRDB Module](architecture/rrdb.md) - Residual in Residual Dense Block
- [PixelShuffleUpsample](architecture/pixel_shuffle_upsample.md) - Upsampling module

## Training

- [Training Overview](training/overview.md) - Training strategy and pipeline
- [Training Configuration](training/configuration.md) - Hyperparameters and settings
- [Data Handling](training/data_handling.md) - Data loading and augmentation

## Inference

- [Inference Guide](inference/overview.md) - How to run inference
- [Model Loading](inference/loading_models.md) - Loading checkpoints

## Evaluation

- [Evaluation Metrics](evaluation/metrics.md) - PSNR, SSIM, LPIPS, Sharpness
- [Performance Results](evaluation/results.md) - Benchmark results and comparisons

## Reference

- [Model Files](models/available_models.md) - Checkpoint descriptions
- [Development Setup](development/environment_setup.md) - Environment and dependencies
