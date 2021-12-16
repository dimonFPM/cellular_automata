import cv2

import numpy as np

kernel = np.ones((5, 5), np.uint8)

img = cv2.imread('../src/cow).jpg')
# img = cv2.GaussianBlur(img, (17, 17), 0)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.Canny(img, 100, 100)
img = cv2.dilate(img, kernel, iterations=1)
img = cv2.erode(img, kernel, iterations=1)
print(img.shape)
cv2.imshow('', img)
cv2.waitKey(0)

# t = 1000
# for i in range(t):
#     mov = cv2.VideoCapture(i)
#     check, img = mov.read()
#     if check==True:
#         print(i, check)

# mov = cv2.VideoCapture(700)
# mov.set(3, 1500)  # 3-ширина
# mov.set(4, 500)  # 4-высота
# while True:
#     success, img = mov.read()
#     cv2.imshow('W', img)
#     # print(success)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
