import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("../Assignment/Testimage/image_Peppers512rgb.png", 0)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))


def imageErosion(image, kernel, iterations = 1):
    return cv2.erode(image, kernel=kernel, iterations=iterations)

def imageDilation(image, kernel, iterations = 1):
    return cv2.dilate(image, kernel=kernel, iterations=iterations)
    
def imageOpening(image, iterations = 1):
    kernel = np.ones((3, 3), np.uint8)
    erosion = imageErosion(image, kernel, iterations)
    return imageDilation(erosion, kernel, iterations)
    
def imageClosing(image, iterations = 1):
    kernel = np.ones((3, 3), np.uint8)
    dilation = imageDilation(image, kernel, iterations)
    return imageErosion(dilation, kernel, iterations)

in_deoc = np.int(input("1.(Erosion), 2.(Dilation), 3.(Open), 4.(Close) 번호입력 : "))
in_No = np.int(input("횟수 : "))

image_cp = image.copy()

for i in range(in_No):
    if in_deoc == 1:
        image_cp = imageErosion(image_cp, kernel)
    elif in_deoc == 2:
       image_cp = imageDilation(image_cp, kernel)
    elif in_deoc == 3:
        image_cp = imageOpening(image_cp)
    elif in_deoc == 4:
        image_cp = imageClosing(image_cp)

cv2.imshow("result", image_cp)
cv2.waitKey()
cv2.destroyAllWindows()
