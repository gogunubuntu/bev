import numpy as np
import cv2
from time import sleep
dist = np.array([[-0.381933396278364, 0.126129477059521, 0, 0, 0]])
mtx = np.array(
    [
        [437.424632750524, 0, 332.897790059753],
        [0, 439.447041265684, 225.568175116187],
        [0, 0, 1],
    ]
)

newmtx, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, (640, 480), 0, (640, 480))
while True: 
    sleep(1)
    print("dist: ", dist)
    print("ori mtx:", mtx)
    print("new mtx:", newmtx)

capture = cv2.VideoCapture(
    "/home/nscl2004/Desktop/sample_serving_video/samples/13_16_48Right.mp4"
)
capture.set(cv2.CAP_PROP_AUTO_WB, 0)
capture.set(cv2.CAP_PROP_TEMPERATURE, 3800)


while True:
    ret, img = capture.read()
    cv2.imshow("distort", img)
    dst = cv2.undistort(img, mtx, dist, None, newmtx)
    cv2.imshow("undistort", dst)
    key = cv2.waitKey(1)
    if key == 27:
        break
capture.release()
