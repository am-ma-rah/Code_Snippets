import os
import pandas as pd
Crating a csv file of mnist dataset
path = 'trainingSample\\'
image = []
label = []

for root, directories, files in os.walk(path):
#     print(f'Total Directories: {directories}')
#     print(root)
    for name in files:
#         print(name)
        x = os.path.join(root,name)
        image.append(x)
#         print(x)
        label.append(x.split('\\')[-2])

dict = {'x': image , 'y': label}
df = pd.DataFrame(dict)
df.to_csv('mnist.csv')


# Import Necessary Libraries

from __future__ import print_function, division
import os
import torch
import torch.nn as nn
import torch.nn.functional as F
import pandas as pd
from skimage import io, transform
import numpy as np
import matplotlib.pyplot as plt
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms, utils

# Ignore warnings
import warnings
warnings.filterwarnings("ignore")

plt.ion()   # interactive mode


# GPU
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')


# Dataset Class
class my_dataset(Dataset):
    def __init__(self , mnist , transform = None):
        self.mnist = pd.read_csv(mnist)
        self.transform = transform 
        
    def __len__(self):
        return len(self.mnist)
        
    def __getitem__(self, idx):
        image_path = self.mnist.iloc[idx , 1]
        x = io.imread(image_path)
        y = self.mnist.iloc[idx,2]
        return (x,y)


# Model Architecture
class CNN(nn.Module):
    def __init__(self , in_channels = 1 , num_classes = 10 ):
        super(CNN , self).__init__()
        self.conv1 = nn.Conv2d(in_channels = 1 , out_channels = 8 , kernel_size = (3,3) , stride = (1,1) , padding = (1,1))
        self.pool = nn.MaxPool2d(kernel_size = (2,2) , stride = (2,2))
        
        self.conv2 = nn.Conv2d(in_channels = 8 , out_channels = 16 , kernel_size = (3,3) , stride = (1,1) , padding = (1,1))
        self.fc1 = nn.Linear(16*7*7 , num_classes)
        
        
    def forward(self , x):
        x = F.relu(self.conv1(x))
        x = self.pool(x) 
        x = F.relu(self.conv2(x))
        x = self.pool(x) 
        x = x.reshape(x.shape[0], -1)
        x = self.fc1(x) 

        return x


# Hyperparameters
# csv file containg images path and respective labels
mnist = 'mnist.csv' 

# Dataset Object
dataset = my_dataset(mnist)
# Hyperparamets 
num_classes = 10
in_channels = 1
learning_rate = 0.001
batch_size = 32
num_epochs = 20


# Train Test Split
train_size = int(0.8 * len(dataset))
test_size = len(dataset) - train_size
train_dataset, test_dataset = torch.utils.data.random_split(dataset, [train_size, test_size])


# Data Loader
train_loader = DataLoader( dataset = train_dataset , batch_size = batch_size , shuffle = True)
test_loader = DataLoader(dataset = test_dataset , batch_size = batch_size , shuffle = True)


# Model
model = CNN(in_channels=in_channels, num_classes=num_classes).to(device)


# Loss and Optimizer
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters() , lr = learning_rate)


# Model Training
for epoch in range(num_epochs):
    for batch_idx , (data , targets) in enumerate(train_loader):
        data = torch.unsqueeze(data, 1)
        data = data.float()
        data = data.to(device = device)
    
        targets = targets.to(device = device)
        
        #forward
        scores = model(data)
        loss = criterion(scores, targets)
        
        #backward
        optimizer.zero_grad()
        loss.backward()
        
        #gradient descent or adam step
        optimizer.step()
    print(f'Epoch No. : {epoch} , Loss :{loss}')


# Accuracy Function
def check_accuracy(loader , model):
    num_correct = 0
    num_samples = 0
    model.eval()
    
    with torch.no_grad():
        for x,y in loader:
            x = x.to(device = device)
            x = torch.unsqueeze(x, 1)
            x = x.float()
            y = y.to(device = device)
            
            scores = model(x)
            _ , predictions = scores.max(1)
            num_correct += (predictions==y).sum()
            num_samples += predictions.size(0)
            
        return num_correct/num_samples


# Training Accuracy
print(f'Accuracy on Training Set:{check_accuracy(train_loader , model)*100:.2f}')


# Test Accuracy
print(f'Accuracy on Test Set:{check_accuracy(test_loader , model)*100:.2f}')