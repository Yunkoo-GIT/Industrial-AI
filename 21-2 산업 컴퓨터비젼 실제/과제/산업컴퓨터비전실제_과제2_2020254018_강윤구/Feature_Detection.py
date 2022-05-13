import cv2
import numpy as np

img1 = cv2.imread('../data/stitching/newspaper1.jpg', cv2.IMREAD_COLOR)

grey1 = cv2.imread('../data/stitching/newspaper1.jpg', 0)
grey = cv2.resize(img1, dsize=(0, 0), fx=0.5, fy=0.5)
edge3 = cv2.Canny(grey, 170, 200)
cv2.imshow('Canny Edge3', edge3)
cv2.waitKey(0)
cv2.destroyAllWindows()


img = cv2.resize(img1, dsize=(0, 0), fx=0.5, fy=0.5)
corners = cv2.cornerHarris(cv2.cvtColor(img, cv2.COLOR_RGB2GRAY), 2, 3, 0.04)

corners = cv2.dilate(corners, None)

show_img = np.copy(img)
show_img[corners>0.1*corners.max()]=[0,0,255]

corners = cv2.normalize(corners, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
show_img = np.hstack((show_img, cv2.cvtColor(corners, cv2.COLOR_GRAY2BGR)))

cv2.imshow('Harris corner detector', show_img)
if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()