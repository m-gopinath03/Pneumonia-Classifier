##This block is only for access of files using google drive
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from google.colab import auth
from oauth2client.client import GoogleCredentials

import matplotlib.pyplot as plt
import numpy as np;
from random import shuffle;
from tqdm import tqdm;
import pickle 

auth.authenticate_user()
gauth = GoogleAuth()
gauth.credentials = GoogleCredentials.get_application_default()
drive = GoogleDrive(gauth)

train_Normal_File = drive.CreateFile({'id': '1tQaJjOhCDUfutK4gUmUxbORhO31Fc255'});
train_Pneumonia_File = drive.CreateFile({'id': '1-TcsGSDO2oktO9td99BvOyCq4-jACOin'});

test_Normal_File = drive.CreateFile({'id': '1gsGgnn5sCuLM4lcr-0FEhuqCs3FLPXJp'});
test_Pneumonia_File = drive.CreateFile({'id': '1V8yWCFv2VO7qtBN4aclAdfhA3EpXNxdH'});

train_Normal_File.GetContentFile("X_train_N.npy");
train_Pneumonia_File.GetContentFile("X_train_P.npy");
test_Normal_File.GetContentFile("X_test_N.npy");
test_Pneumonia_File.GetContentFile("X_test_P.npy");

X_train_N = np.load("X_train_N.npy");     # Normal X-rays: Training
X_train_P = np.load("X_train_P.npy");     # Pneumonia X-rays: Training

X_test_N = np.load("X_test_N.npy");       # Normal X-rays: Testing
X_test_P = np.load("X_test_P.npy");       # Pneumonia X-rays: Testing

print("X_train_Normal shape: ", X_train_N.shape);
print("X_train_PNEUMONIA shape: ", X_train_P.shape);
print("X_test_Normal shape: ", X_test_N.shape);
print("X_test_PNEUMONIA shape: ", X_test_P.shape);

# Plotting n(=10) X-rays from all databases:
# Row1:X_train_Normal, Row2:X_train_Pneumonia, Row3:X_test_Normal, Row4:X_test_Pneumonia

n = 10
plt.figure(figsize=(20, 10))
for i in range(n):
    ax = plt.subplot(4, n, i+1)
    plt.imshow(X_train_N[i,:,:].reshape(150,150), cmap='gray')
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    ax = plt.subplot(4, n, i+1*n+1)
    plt.imshow(X_train_P[i,:,:].reshape(150,150), cmap='gray')
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    ax = plt.subplot(4, n, i+2*n+1)
    plt.imshow(X_test_N[i,:,:].reshape(150,150), cmap='gray')
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    ax = plt.subplot(4, n, i+3*n+1)
    plt.imshow(X_test_P[i,:,:].reshape(150,150), cmap='gray')
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
