# 개발 환경 구성
# pip install opencv-python
# pip install numpy

import cv2
import numpy as np

image = cv2.imread('/Users/lordk/Github/BARAM_SEMINAR_DEEPLEARNING/images/robot.jpg')

horizontal_filter = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])
vertical_filter = np.array([[1, 0, -1], [1, 0, -1], [1, 0, -1]])

horizontal_result = cv2.filter2D(image, -1, horizontal_filter)
vertical_result = cv2.filter2D(image, -1, vertical_filter)

cv2.imwrite('horizontal_pattern.jpg', horizontal_result)
cv2.imwrite('vertical_pattern.jpg', vertical_result)
