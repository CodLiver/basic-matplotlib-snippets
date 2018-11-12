""" ##### OPENCV2 IMAGE FORMAT TO PIL FORMAT ###### """
# sadly sometimes the formats are not compatible :))))))))
# so this following snippets to change image's cv2 format to PIL format. Useful if you want to normalize as mentioned. If better method outside, please pull request it.
import PIL,cv2


#reads image in cv2 BGR format
img = cv2.imread(PATH)
# convets to PIL format. Apparently PIL is in RGB format.
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# cv2 are array, PIL is not array as seen.
img = Image.fromarray(img)

""" ## or simply use this. Original PIL open Image. ##"""
img = Image.open(PATHVAL+exampleImage)

""" ##### Image Addition ###### """
"(image1, opacity1, image2, opacity2, gamma value)"
added = cv2.addWeighted(img1, 1 ,img2, 1,0)

""" ##### Image Resize ###### """
resizedImg = cv2.resize(img,(newX,newY))

""" ##### Image display ##### """
cv2.imshow("Window Title",img)
cv2.waitKey(0) #if zero, img will stay until you press any key. if >0, then it will wait that much time and closes.
