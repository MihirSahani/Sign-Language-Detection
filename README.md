# Sign Language Detection Project

## Overview

The Sign Language Detection Project is designed to automatically interpret sign language gestures and translate them into corresponding letters or numbers in real-time. This project includes two main Python scripts, `build_model.py` and `test_model.py`, making it easy to build and deploy a sign language recognition model.

## Project Components

### 1. Data Collection and Preprocessing

- Hand sign photos have been collected and transformed into CSV files.
- The dataset has been divided into training and testing subsets for model evaluation.

### 2. Model Building

- `build_model.py` reads and normalizes the dataset, and generates addition data from current dataset.
- A deep learning model is constructed, trained, and saved in the "Resources" folder.

### 3. Real-time Sign Language Detection

- `test_model.py` is used to test and deploy the model for real-time sign language detection.
- The script accesses the camera feed to recognize and interpret signs.

## Dependencies

Ensure you have the following dependencies installed:

- Python (3.x)
- `numpy`
- `pandas`
- `tensorflow` (or `keras` with `tensorflow` backend)
- `scikit-learn`
- `opencv-contrib-python`

You can install these dependencies manually or use the provided `signlanguage.sh` script for automated setup.

## Usage
To run the project, simply execute the `signlanguage.sh` script. This script automates virtual environment setup, dependency installation, and model execution. It simplifies the process of running the sign language detection model with real-time camera input.

Firstly clone the repository
```bash
git clone git@github.com:Krakenmaregit/Sign-Language-Interpretor.git
```


To provide execution permission to the script, use:

```bash
chmod u+x signlanguage.sh
```
Lastly execute the script

```bash
./signlanguage.sh
```

## Issues and Contributions

If you encounter issues or have suggestions for improvements, please feel free to open an issue in the project repository. Contributions and enhancements are also welcome through pull requests.
