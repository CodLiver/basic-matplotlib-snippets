"""you can find how to save/load in https://pytorch.org/tutorials/beginner/saving_loading_models.html"""

import torch

"""this is recommended, because if you just save without state_dict(), it may get broken."""
torch.save(model.state_dict(), PATH)

""""load part"""
model_weights = torch.load("model_weights.m")# like PATH
model = models.resnet34(pretrained=True)
# state the model, load it and add the weights
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

""" Data Parallelism"""
# WHEN YOU HAVE MULTIPLE GPU. YOU DONT. SO DONT USE IT.
model = torch.nn.DataParallel(model).cuda()

# if you save whole model, it will have module.COMPONENT. this to remove Data Parallelism
try:
    state_dict = modell.module.state_dict()
except AttributeError:
    state_dict = modell.state_dict()
# alternatively.

oldmodel=beSavedModel.copy()
newmodel={}
for each in oldmodel:
    newmodel[each[7:]]=beSavedModel.pop(each)
model.load_state_dict(newmodel)
torch.save(model.state_dict(),"final.m")
#this to save module.module.COMPONENT that is caused by Data Parallelism

""" How to produce a heatmap by ptrblck"""
model = models.resnet34(pretrained=True)
model = model.cuda()
device = torch.device("cuda")
model.eval()

trns=transforms.ToTensor()
images=trns(Image.open("image.png"))

criterion = nn.BCEWithLogitsLoss()

def normalize_output(img):
    img = img - img.min()
    img = img / img.max()
    return img

# Visualize feature maps
activation = {}
def get_activation(name):
    def hook(model, input, output):
        activation[name] = output.detach()
    return hook


observe="layer4"#conv1 or any layer in the __init__ area.
model.layer4.register_forward_hook(get_activation(observe))

with torch.no_grad():
    images=images.cuda(device)
    images.unsqueeze_(0)
    output = model(images)

# some representation on plt.
act = activation[observe].squeeze()
for each in range(50):
    fig, axarr = plt.subplots(5)
    counter=0
    for idx in range(5*each,5*each+5):
        axarr[counter].imshow(act[idx].cpu())
        counter+=1
    plt.show()
