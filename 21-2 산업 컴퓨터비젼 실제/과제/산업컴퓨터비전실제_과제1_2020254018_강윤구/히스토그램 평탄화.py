import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("../Assignment/Testimage/image_Peppers512rgb.png", cv2.IMREAD_COLOR)
image_eq = image.copy()

b, g, r = cv2.split(image)

in_rgb = input("r, g, b 중 하나를 입력하시오 : ")


def output_p():

    hist, bins = np.histogram(coloreq, 256, [0, 255])
    plt.fill(hist)
    plt.xlabel('histogram')
    plt.show()


    cv2.imshow("orginal image", image)
    cv2.imshow("equalize color=" + in_rgb, image_eq)
    cv2.waitKey()
    cv2.destroyAllWindows()
    
if in_rgb == "b":
    coloreq = cv2.equalizeHist(b)
    image_eq = cv2.merge((coloreq, g, r))
    output_p()
elif in_rgb == "g":
    coloreq = cv2.equalizeHist(g)
    image_eq = cv2.merge((b, coloreq, r))
    output_p()
elif in_rgb == "r":
    coloreq = cv2.equalizeHist(r)
    image_eq = cv2.merge((b, g, coloreq))
    output_p()
else:
    print('잘못 입력 하였습니다.')

