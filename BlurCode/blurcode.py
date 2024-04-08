
import cv2
import numpy as np


image_path = "/Users/lordk/Github/BARAM_SEMINAR_DEEPLEARNING/images/robot.jpg"
image = cv2.imread(image_path)

# 3x3 블러(평균화) 필터 정의
blur_filter = np.ones((3, 3), np.float32) / 9

# 필터 적용 - cv2.filter2D 함수 사용
blurred_image = cv2.filter2D(image, -1, blur_filter)

cv2.imwrite("blurred_image.jpg", blurred_image)
