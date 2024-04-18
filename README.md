# Chest X-ray Classification using Convolutional Neural Networks


## Overview

This repository contains the implementation of a Convolutional Neural Network (CNN) for classifying chest X-ray images into two categories: normal and pneumonia. The model is designed to assist in the automated diagnosis of pneumonia based on X-ray images.

## Dataset

The dataset used for training and testing the model consists of chest X-ray images sourced from various medical repositories. It is divided into two classes:

- **Normal**: X-ray images of healthy individuals.
- **Pneumonia**: X-ray images showing signs of pneumonia infection.

## Model Architecture

The CNN model architecture is as follows:

- **Input Layer**: Accepts grayscale chest X-ray images with dimensions 150x150 pixels.
- **Convolutional Layers**: Four convolutional layers with increasing depth followed by max-pooling layers to extract features from the input images.
- **Fully Connected Layers**: Two dense layers with 512 neurons each, followed by dropout regularization to prevent overfitting.
- **Output Layer**: Two neurons representing the probability of the input image belonging to each class (normal or pneumonia).

## Training

The model is trained using the Adam optimizer and categorical cross-entropy loss function. The training dataset is augmented to improve model generalization, and the training process is monitored using both training and validation data. Training is conducted for 300 epochs with a batch size of 80.

## Evaluation

After training, the model is evaluated on a separate testing dataset to assess its performance. The evaluation metrics include accuracy, precision, recall, and F1-score.

## Results

The trained model achieves an accuracy of approximately 77.24% on the testing dataset, indicating its effectiveness in classifying chest X-ray images.

## Usage

1. **Data Preparation**: Ensure that the chest X-ray images are properly labeled and organized into training and testing directories.
2. **Model Training**: Execute the provided training script to train the CNN on the dataset.
3. **Model Evaluation**: After training, evaluate the model's performance using the testing dataset to assess its accuracy and other relevant metrics.
4. **Inference**: Once trained, the model can be used to classify new chest X-ray images into normal or pneumonia categories.

## Dependencies

- Python 3.x
- TensorFlow 2.x
- NumPy
- Matplotlib
- PyDrive (for accessing files from Google Drive)
- Google Colab (for running the code in a Colab environment)

## License

This project is licensed under the Department of Biomedical, IIT Ropar.
