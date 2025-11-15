# MARPOL_Violation_Detection

MARPOL_Violation_Detection is an AI-powered project designed to detect maritime pollution violations automatically. The system leverages computer vision and deep learning techniques to identify environmental violations, supporting compliance with MARPOL regulations.

## Features

- Detects marine pollution violations from images or videos.
- Uses state-of-the-art deep learning models for object detection and classification.
- Generates reports for potential violations.
- Easy to integrate with existing maritime monitoring systems.

## Project Structure

MARPOL_Violation_Detection/
│
├── src/ # Source code
│ ├── train.py # Model training script
│ ├── validate.py # Model validation script
│ └── ...
├── data/ # Dataset used for training/validation
├── models/ # Trained models
├── README.md # Project documentation
└── requirements.txt # Python dependencies


## Installation

1. Clone the repository:

```bash
git clone https://github.com/nikhil242000/MARPOL_Violation_Detection.git
cd MARPOL_Violation_Detection

2) Create a virtual environment and activate it:
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate

3)Install dependencies:
pip install -r requirements.txt

4)Usage

Training the model:

python src/train.py

5)Validating the model:

python src/validate.py
