import cv2
import numpy as np

img1 = cv2.imread('../data/stitching/dog_a.jpg', cv2.IMREAD_COLOR)
img2 = cv2.imread('../data/stitching/dog_b.jpg', cv2.IMREAD_COLOR)

prev_pts = None
prev_gray_frame = None
tracks = None

frame = np.copy(img1)
frame = cv2.resize(frame, (0,0), None, 0.5, 0.5)
gray_frame = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray_frame = cv2.resize(gray_frame, (0,0), None, 0.5, 0.5)
prev_gray_frame = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
prev_gray_frame = cv2.resize(prev_gray_frame, (0,0), None, 0.5, 0.5)

#Good Feature to Tracking, Pyramid Lucas-Kanade, Optical Flow
pts = cv2.goodFeaturesToTrack(gray_frame, 500, 0.05, 10)
pts = pts.reshape(-1, 1, 2)

pts, status, errors = cv2.calcOpticalFlowPyrLK(
    prev_gray_frame, gray_frame, pts, None, winSize=(15,15), maxLevel=5,
    criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

good_pts = pts[status == 1]

if tracks is None: tracks = good_pts
else: tracks = np.vstack((tracks, good_pts))
for p in tracks:
    cv2.circle(frame, (p[0], p[1]), 3, (0, 255, 0), -1)

cv2.imshow('frame', frame)
cv2.waitKey()

#Farneback
opt_flow = cv2.calcOpticalFlowFarneback(
    prev_gray_frame, gray_frame, None, 0.5, 5, 13, 10, 5, 1.1,
    cv2.OPTFLOW_USE_INITIAL_FLOW)
opt_flow = cv2.calcOpticalFlowFarneback(
    prev_gray_frame, gray_frame, opt_flow, 0.5, 5, 13,10, 5, 1.1,
    cv2.OPTFLOW_USE_INITIAL_FLOW)

stride=40
for index in np.ndindex(opt_flow[::stride, ::stride].shape[:2]):
    pt1 = tuple(i * stride for i in index)
    delta = opt_flow[pt1].astype(np.int32)[::-1]
    pt2 = tuple(pt1 + 10 * delta)  # 10==

    if 2 <= cv2.norm(delta) <= 10:
        cv2.arrowedLine(frame, pt1[::-1], pt2[::-1], (0, 0, 255), 5, cv2.LINE_AA, 0, 0.4)

norm_opt_flow = np.linalg.norm(opt_flow, axis=2)
norm_opt_flow = cv2.normalize(norm_opt_flow, None, 0, 1, cv2.NORM_MINMAX)

cv2.imshow('optical flow', frame)
cv2.imshow('optical flow magnitude', norm_opt_flow)
cv2.waitKey()

#DualTVL1, Optical Flow
flow_DualTVL1 = cv2.createOptFlow_DualTVL1()
opt_flow = flow_DualTVL1.calc(prev_gray_frame, gray_frame, None)
flow_DualTVL1.setUseInitialFlow(True)
opt_flow = flow_DualTVL1.calc(prev_gray_frame, gray_frame, opt_flow)

for index in np.ndindex(opt_flow[::stride, ::stride].shape[:2]):
    pt1 = tuple(i * stride for i in index)
    delta = opt_flow[pt1].astype(np.int32)[::-1]
    pt2 = tuple(pt1 + 10 * delta)  # 10==

    if 2 <= cv2.norm(delta) <= 10:
        cv2.arrowedLine(frame, pt1[::-1], pt2[::-1], (0, 0, 255), 5, cv2.LINE_AA, 0, 0.4)

norm_opt_flow = np.linalg.norm(opt_flow, axis=2)
norm_opt_flow = cv2.normalize(norm_opt_flow, None, 0, 1, cv2.NORM_MINMAX)

cv2.imshow('optical flow', frame)
cv2.imshow('optical flow magnitude', norm_opt_flow)
cv2.waitKey()
cv2.destroyAllWindows()