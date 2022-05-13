import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("../Assignment/Testimage/image_Peppers512rgb.png").astype(np.float32) / 255


noised = (image + 0.2 * np.random.rand(*image.shape).astype(np.float32))
noised = noised.clip(0, 1)


in_dim = np.int(input("Diameter 입력하시오 : "))
S_color = np.float(input("Sigma Color 입력하시오 : "))
S_space = np.float(input("Sigma Space 입력하시오 : "))

bilat = cv2.bilateralFilter(noised, in_dim, S_color, S_space)

cv2.imshow("original", image)
cv2.imshow("noised", noised)
cv2.imshow("bilateralFilter", bilat)
cv2.waitKey()
cv2.destroyAllWindows()