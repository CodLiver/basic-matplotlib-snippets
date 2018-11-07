##you can find how to save/load in https://pytorch.org/tutorials/beginner/saving_loading_models.html

import torch

# this is recommended, because if you just save without state_dict(), it may get broken.
torch.save(model.state_dict(), PATH)

##load part
model = TheModelClass(*args, **kwargs)
model.load_state_dict(torch.load(PATH))
model.eval()

##general problems with the load part. You might think what is modelclass.
# its basically a class that has __init__(), forward(). you need to add your previous model/layers to totally load your model.
# if you use pretrained resnet etc. NOW I AM SEARCHING HOW TO FIND.
