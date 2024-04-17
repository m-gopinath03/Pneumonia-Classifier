# Pneumonia-Classifier

## Chest X-Ray Image Classifier

## Overview
This project aims to develop a Convolutional Neural Network (CNN) based classifier to distinguish between normal and pneumonia cases using chest X-ray images. The dataset consists of approximately 5500 X-ray images categorized into two classes: Pneumonia and Normal. These images were obtained from pediatric patients aged one to five years old from Guangzhou Women and Children’s Medical Center, Guangzhou, as part of their routine clinical care.

## Dataset
The dataset is organized into two folders: `train` and `test`, each containing subfolders for each image category (Pneumonia/Normal). The chest X-ray images are in anterior-posterior view. Before training the model, all images underwent quality control screening to remove low-quality or unreadable scans. Additionally, the diagnoses for the images were graded by two expert physicians. An evaluation set was also checked by a third expert to account for any grading errors.

## Model Development
The classifier was developed using a CNN architecture. The model was trained on the training dataset and evaluated on the test dataset to assess its performance in distinguishing between normal and pneumonia cases.

## Usage
To use the classifier:
1. Ensure Python and necessary libraries (e.g., TensorFlow, Keras) are installed.
2. Clone this repository.
3. Navigate to the project directory.
4. Run the provided script to train and evaluate the model.

```bash
python train_model.py
