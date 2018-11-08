from torch.autograd import Variable
from torch.utils.data import Dataset,DataLoader
from torchvision import transforms
from PIL import Image
import cv2,time,os,shutil,torch,csv
import numpy as np
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import torchvision.models as models
import torch.backends.cudnn as cudnn
import torchvision.datasets as datasets

class Classifier():
    """
    Classifier Class:
    __init__(PATH, modelPATH)
    Parameters:
    PATH to dataset
    modelPATH to model

    sets normalization,model,device,transformation vars.

    cv2PIL(img)
    Parameters:
    img=cv2 type img
    OUT: PIL type image

    unitClassifier(image)
    image=cv2 image from anywhere.
    deploys to DL model, gets prediction
    OUT: predicted result from model

    """
    def __init__(self, PATH, modelPATH):
        super(Classifier, self).__init__()
        self.PATH=PATH
        self.normalize = transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                         std=[0.229, 0.224, 0.225])

        self.transformations=transforms.Compose([
            transforms.RandomHorizontalFlip(),
            transforms.Resize(256),
            transforms.RandomCrop(224),
            transforms.ToTensor(),
            self.normalize,
        ])

        self.model=torch.load(modelPATH)
        self.device = torch.device("cuda:0")

    def cv2PIL(self,img):
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        return img

    def unitClassifier(self,images):
        """
        IN: Image (cv2 format)
        OUT: Label
        """
        if type(images) is np.ndarray:
            images=self.transformations(self.cv2PIL(images)).unsqueeze_(0)
        else:
            images=self.transformations(images).unsqueeze_(0)
            
        with torch.no_grad():
            images=images.cuda(self.device)
            outputs = self.model(images)
            _, predicted = torch.max(outputs.data, 1)
            predicted=predicted.cpu().numpy()

        return predicted

    def batchClassifier(self,PATH2BATCH):
        """
        batch classifier without using datasets. Can be used for unsupervised classification.
        IN: path to file
        OUT: result.csv file for name of file and its prediction
        """
        print("batchClassifier()")
        totalList=os.listdir(PATH2BATCH)
        with open('result.csv', mode='w') as resultsCSV:
            resultsCSV = csv.writer(resultsCSV, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for eachPicture in totalList:
                img = Image.open(PATH2BATCH+eachPicture)
                resultsCSV.writerow([eachPicture, self.unitClassifier(img)])
        return "file was created"
