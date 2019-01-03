"""you can find how to save/load in https://pytorch.org/tutorials/beginner/saving_loading_models.html"""

import torch

"""this is recommended, because if you just save without state_dict(), it may get broken."""
torch.save(model.state_dict(), PATH)

""""load part"""
model = TheModelClass(*args, **kwargs)
model.load_state_dict(torch.load(PATH))
model.eval()

""" #### general problems with the load part. You might think what is modelclass. ###"""
""" 
    its basically a class that has __init__(), forward(). you need to add your previous model/layers to totally load your model.
    if you use pretrained resnet etc.: NOW I AM SEARCHING HOW TO FIND.
    currently just use the not recommended version which is: save the model with PATH. prone to errors, if the path is broken.
"""


""" # NORMALIZATION OF IMAGES # """

#some libraries to import
from torchvision import transforms
from PIL import Image

#default model values
normalize = transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                 std=[0.229, 0.224, 0.225])

#transformation values. you should normalize your images before sending to model
transformations=transforms.Compose([
    transforms.RandomHorizontalFlip(),
    #in order to fit the images well into our model, we need to have same size images. there are other methods that welcome different size images, but I will explain that later. Haven't found the answer yet. 
    transforms.Resize(256),
    transforms.RandomCrop(224),
    # If this method comes before Resize(size) method, it throws error. ALL images that are inputted in this method, should be in PIL format. Resize Inputs PIL, Outputs PIL. toTensor IN: PIL, OUT: tensor type. 
    transforms.ToTensor(),
    #normalize it
    normalize,
])

# in the end when you deploy your image to your model validation func
model(img.unsqueeze_(0))
# unsqueze() was given because "RuntimeError: expected stride to be a single integer value or a list of 1 values to match the convolution dimensions, but got stride=[2, 2]" error is recieved.

""" ##### OPENCV2 IMAGE FORMAT TO PIL FORMAT ###### """
# sadly sometimes the formats are not compatible :))))))))
# so this following snippets to change image's cv2 format to PIL format. Useful if you want to normalize as mentioned. If better method outside, please pull request it.

#reads image in cv2 BGR format
img = cv2.imread(PATH)
# convets to PIL format. Apparently PIL is in RGB format.
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# cv2 are array, PIL is not array as seen.
img = Image.fromarray(img)
# transformation as told.
img=transformations(img)

""" ## or simply use this. Original PIL open Image. ##"""
img = Image.open(PATHVAL+exampleImage)
img = transformations(torch.from_numpy(img))


