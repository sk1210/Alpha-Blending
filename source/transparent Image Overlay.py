__author__ = 'Pytech Solution'
import cv2
import numpy as np

backgroundImgName = "1234.jpg"
pngImageName =  "overlay.png"
logo = "logo.png"

def transparentOverlay(src , overlay , pos=(0,0),scale = 1):
    """
    :param src: Input Color Background Image
    :param overlay: transparent Image (BGRA)
    :param pos:  position where the image must be put.
    :return: Resultant Image
    """
    overlay = cv2.resize(overlay,(0,0),fx=scale,fy=scale)
    h,w,_ = overlay.shape  # Size of pngImg
    rows,cols,_ = src.shape  # Size of background Image
    x,y = pos[0],pos[1]    # Position of PngImage

    for i in range(h):
        for j in range(w):
            if x+i >= rows or y+j >= cols:
                continue
            alpha = float(overlay[i][j][3]/255)
            src[x+i][y+j] = alpha*overlay[i][j][:3]+(1-alpha)*src[x+i][y+j]
    return src

bImg = cv2.imread(backgroundImgName)
pngImage = cv2.imread(pngImageName , cv2.IMREAD_UNCHANGED)
logoImage = cv2.imread(logo,cv2.IMREAD_UNCHANGED)

result = transparentOverlay(bImg,pngImage,(0,300),0.7)
result = transparentOverlay(bImg,logoImage,(400,800),2)

cv2.namedWindow("Result",cv2.WINDOW_NORMAL)
cv2.imshow("Result" ,result)
cv2.waitKey()
cv2.destroyAllWindows()

cv2.imwrite("result.jpg",result)