import cv2
import numpy as np

images = []
images.append(cv2.imread('../data/stitching/s1.jpg', cv2.IMREAD_COLOR))
images.append(cv2.imread('../data/stitching/s2.jpg', cv2.IMREAD_COLOR))

stitcher = cv2.createStitcher()
ret, pano = stitcher.stitch(images)

if ret == cv2.STITCHER_OK:
    pano = cv2.resize(pano, dsize=(0, 0), fx=0.3, fy=0.3)
    cv2.imshow('s', pano)
    cv2.waitKey()

    cv2.destroyAllWindows()
else:
    print('Error during stiching')