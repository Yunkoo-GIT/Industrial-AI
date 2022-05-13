import cv2
import numpy as np
import matplotlib.pyplot as plt

img1 = cv2.imread('../data/stitching/s1.jpg', cv2.IMREAD_COLOR)
img2 = cv2.imread('../data/stitching/s2.jpg', cv2.IMREAD_COLOR)

#SURF
surf = cv2.xfeatures2d.SURF_create(10000)
surf.setExtended(True)
surf.setNOctaves(3)
surf.setNOctaveLayers(10)
surf.setUpright(False)

keyPoints, descriptors = surf.detectAndCompute(img1, None)
img_surf1 = cv2.drawKeypoints(img1, keyPoints, None, (255, 0, 0),
                              cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

keyPoints, descriptors = surf.detectAndCompute(img2, None)
img_surf2 = cv2.drawKeypoints(img2, keyPoints, None, (255, 0, 0),
                              cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
#SIFT
sift = cv2.xfeatures2d.SIFT_create()
keyPoints, descriptors = sift.detectAndCompute(img1, None)
img_sift1 = cv2.drawKeypoints(img1, keyPoints, None, (255, 0, 0),
                             cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

sift = cv2.xfeatures2d.SIFT_create()
keyPoints, descriptors = sift.detectAndCompute(img2, None)
img_sift2 = cv2.drawKeypoints(img2, keyPoints, None, (255, 0, 0),
                             cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
#ORB
orb = cv2.ORB_create()
orb.setMaxFeatures(200)

keyPoints = orb.detect(img1, None)
keyPoints, descriptors = orb.compute(img1, keyPoints)
img_orb1 = cv2.drawKeypoints(img1, keyPoints, None, (0, 0, 255),
                            cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

keyPoints = orb.detect(img2, None)
keyPoints, descriptors = orb.compute(img2, keyPoints)
img_orb2 = cv2.drawKeypoints(img2, keyPoints, None, (0, 0, 255),
                            cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

#MATCH
img_1 = cv2.cvtColor(img_surf1, cv2.COLOR_BGR2GRAY)
img_2 = cv2.cvtColor(img_surf2, cv2.COLOR_BGR2GRAY)

detector = cv2.ORB_create(100)
kps1, fea1 = detector.detectAndCompute(img_1, None)
kps2, fea2 = detector.detectAndCompute(img_2, None)
matcher = cv2.BFMatcher_create(cv2.NORM_HAMMING, False)
matches = matcher.match(fea1, fea2)

pts1 = np.float32([kps1[m.queryIdx].pt for m in matches]).reshape(-1, 1, 2)
pts2 = np.float32([kps2[m.queryIdx].pt for m in matches]).reshape(-1, 1, 2)

H, mask = cv2.findHomography(pts1, pts2, cv2.RANSAC, 3.0)
dbg_img = cv2.drawMatches(img_1, kps1, img_2, kps2, matches, None)
dbg_img1 = cv2.drawMatches(img_1, kps1, img_2, kps2,
                           [m for i, m in enumerate(matches) if mask[i]], None)

#WARPING
dst = cv2.warpPerspective(dbg_img1, H, (dbg_img.shape[1] * 2, dbg_img.shape[0] * 2))

titles = ['image1_SURF', 'image2_SURF', 'All match', 'Filtered match', 'warped_img']
images = [img_1, img_2, dbg_img[:, :, [2, 1, 0]], dbg_img1[:, :, [2, 1, 0]], dst]

plt.figure(figsize=(18, 5))
for i in range(5):
    plt.subplot(1, 5, i + 1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])
plt.show()


img_1 = cv2.cvtColor(img_sift1, cv2.COLOR_BGR2GRAY)
img_2 = cv2.cvtColor(img_sift2, cv2.COLOR_BGR2GRAY)

detector = cv2.ORB_create(100)
kps1, fea1 = detector.detectAndCompute(img_1, None)
kps2, fea2 = detector.detectAndCompute(img_2, None)
matcher = cv2.BFMatcher_create(cv2.NORM_HAMMING, False)
matches = matcher.match(fea1, fea2)

pts1 = np.float32([kps1[m.queryIdx].pt for m in matches]).reshape(-1, 1, 2)
pts2 = np.float32([kps2[m.queryIdx].pt for m in matches]).reshape(-1, 1, 2)

H, mask = cv2.findHomography(pts1, pts2, cv2.RANSAC, 3.0)
dbg_img = cv2.drawMatches(img_1, kps1, img_2, kps2, matches, None)
dbg_img1 = cv2.drawMatches(img_1, kps1, img_2, kps2,
                           [m for i, m in enumerate(matches) if mask[i]], None)

dst = cv2.warpPerspective(dbg_img1, H, (dbg_img.shape[1] * 2, dbg_img.shape[0] * 2))

titles = ['image1_SIFT', 'image2_SIFT', 'All match', 'Filtered match', 'warped_img']
images = [img_1, img_2, dbg_img[:, :, [2, 1, 0]], dbg_img1[:, :, [2, 1, 0]], dst]

plt.figure(figsize=(18, 5))
for i in range(5):
    plt.subplot(1, 5, i + 1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])
plt.show()


img_1 = cv2.cvtColor(img_orb1, cv2.COLOR_BGR2GRAY)
img_2 = cv2.cvtColor(img_orb2, cv2.COLOR_BGR2GRAY)

detector = cv2.ORB_create(100)
kps1, fea1 = detector.detectAndCompute(img_1, None)
kps2, fea2 = detector.detectAndCompute(img_2, None)
matcher = cv2.BFMatcher_create(cv2.NORM_HAMMING, False)
matches = matcher.match(fea1, fea2)

pts1 = np.float32([kps1[m.queryIdx].pt for m in matches]).reshape(-1, 1, 2)
pts2 = np.float32([kps2[m.queryIdx].pt for m in matches]).reshape(-1, 1, 2)

H, mask = cv2.findHomography(pts1, pts2, cv2.RANSAC, 3.0)
dbg_img = cv2.drawMatches(img_1, kps1, img_2, kps2, matches, None)
dbg_img1 = cv2.drawMatches(img_1, kps1, img_2, kps2,
                           [m for i, m in enumerate(matches) if mask[i]], None)

dst = cv2.warpPerspective(dbg_img1, H, (dbg_img.shape[1] * 2, dbg_img.shape[0] * 2))

titles = ['image1_ORB', 'image2_ORB', 'All match', 'Filtered match', 'warped_img']
images = [img_1, img_2, dbg_img[:, :, [2, 1, 0]], dbg_img1[:, :, [2, 1, 0]], dst]

plt.figure(figsize=(18, 5))
for i in range(5):
    plt.subplot(1, 5, i + 1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])
plt.show()