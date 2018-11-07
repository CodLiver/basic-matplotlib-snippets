##continuous graph update
# plt.show(block=False) was deprecated

# import the library
from matplotlib import pyplot as plt 

# switch interactive graph on
plt.ion()
# open the window to top, so no need to do it again or lose the picture
plt.show()

#
# your calculation code 
#

# clear the previous images. was put into top, because hard to see change of any histogram due to rapid clearing.
plt.clf()

# color one will be put later: [MAIN] is the main data, [0] for grayscale
histr = cv2.calcHist([MAIN],[0],None,[256],[150,256])
# plot the histr, plot(histr,color=col) for RGB hists.
plt.plot(histr)
#draw it
plt.draw()
#wait a bit time to see the histr.
plt.pause(0.001)
