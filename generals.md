# Basic error and general practices:

## 1. Import Class from subfolders in Python3
```
example path folder:
main/
    main.py
    subfolder/
          __init__.py
          subFile.py
          subUtil.py    
```
          
always remember to put \_\_init__.py to your subfolders that makes them importable, hence treats them as packages.

always in your sub files aka module files (subFile,subUtil), all files' imports should also contain their head dir's relative path. ```subfile.py =>  import subfolder.subUtil```

Your \_\_init__.py can be empty or ```from .subFile import ClassName```

Class initials are always big.

More info: 

* https://stackoverflow.com/questions/4142151/how-to-import-the-class-within-the-same-directory-or-sub-directory
* https://stackoverflow.com/questions/1260792/import-a-file-from-a-subdirectory
* https://docs.python.org/3/tutorial/modules.html


## 2. Cv2 Errors:
If you receive this error, that means your program couldn't find the image you are referring. check ".png" and ".jpg" extensions in your code.
```
cv2.error: OpenCV(3.4.1) C:\projects\opencv-python\opencv\modules\imgproc\src\resize.cpp:4044: error: (-215) ssize.width > 0 && ssize.height > 0 in function cv::resize
```
