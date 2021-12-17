# import cv2
#
# import numpy as np
#
# kernel = np.ones((5, 5), np.uint8)
#
# img = cv2.imread('../src/cow).jpg')
# # img = cv2.GaussianBlur(img, (17, 17), 0)
# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# img = cv2.Canny(img, 100, 100)
# img = cv2.dilate(img, kernel, iterations=1)
# img = cv2.erode(img, kernel, iterations=1)
# print(img.shape)
# cv2.imshow('', img)
# cv2.waitKey(0)
#
#
# # t = 1000
# # for i in range(t):
# #     mov = cv2.VideoCapture(i)
# #     check, img = mov.read()
# #     if check==True:
# #         print(i, check)
#
# # mov = cv2.VideoCapture(700)
# # mov.set(3, 1500)  # 3-ширина
# # mov.set(4, 500)  # 4-высота
# # while True:
# #     success, img = mov.read()
# #     cv2.imshow('W', img)
# #     # print(success)
# #     if cv2.waitKey(1) & 0xFF == ord('q'):
# #         break
#
# # k = np.ones((3, 3))
# # for i in range(1,1000):
# #     mov = cv2.VideoCapture(i)
# #     check, img = mov.read()
# #     print(f"{i}={check}")
# #     if check == True:
# #         break
# # if check==False:
# #     print("не найдена камера")
#
# for i in range(1001):
#     try:
#         mov = cv2.VideoCapture(i)
#         mov.set(3, 1280)
#         mov.set(4, 720)
#         check, img = mov.read()
#         print(f"{i}={check}")
#         if all((mov, check)):
#             print("камера найдена")
#             break
#     except:
#         print("Ошибка")
#         exit()
#
# if check == False:
#     print("камера на найдена")
#
# print("начало")
# k = np.ones((2, 2))
# while True:
#     check, img = mov.read()
#     if check == False:
#         break
#     img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
#     img = cv2.Canny(img, 60, 60)
#     img = cv2.dilate(img, k, iterations=2)
#     img = cv2.erode(img, k, iterations=2)
#
#     cv2.imshow('', img)
#     if cv2.waitKey(1) & 0xFF == ord("q"):
#         break
#
#     # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     # img = cv2.Canny(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), 50, 50)
#     # img = cv2.dilate(img, k, iterations=1)


# import cv2
#
# # img = cv2.imread("cow).jpg")
# import numpy as np
#
# img = np.zeros((300, 300, 3), dtype="uint8")
# # img[50:100,30:50] = 60, 158, 24
# cv2.rectangle(img, (40, 40), (100, 100), (60, 158, 24), thickness=cv2.FILLED)
# cv2.line(img, (0, img.shape[0] // 2), (200, 200), (255, 0, 0), thickness=5)
# cv2.circle(img, (300, 300), 50, (0, 0, 255), thickness=cv2.FILLED)
# cv2.putText(img, "qqq", (200, 100), cv2.FONT_HERSHEY_TRIPLEX, 0.5, (60, 158, 24))
#
# cv2.imshow("", img)
# # img
# cv2.waitKey(0)

# img = cv2.flip(img, 0)
# def r(img, angle):
#     height, width = img.shape[:2]
#     point = (width // 2, height // 2)
#     mat = cv2.getRotationMatrix2D(point, angle, 1)
#     return cv2.warpAffine(img, mat, (width, height))
# img = r(img, 90)
# img=cv2.flip(cv2.transpose(img),0)


# import cv2
# import numpy as np
#
# img = cv2.imread("cow).jpg")
# # new_img = np.zeros(img.shape, dtype="uint8")
# #
# # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# # img = cv2.GaussianBlur(img, (5, 5), 0)
# # img = cv2.Canny(img, 20, 60)
# #
# # con, hir = cv2.findContours(img, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
# #
# # cv2.drawContours(new_img,con,-1,(60, 158, 24),1)
# #
# # print(new_img.shape)
# # print(img.shape)
# # img=cv2.cvtColor(img,cv2.COLOR_BGR2LAB)
# b, g, r = cv2.split(img)
# img1 = cv2.merge([b, g, r])
# cv2.imshow("", img1)
# cv2.waitKey(0)


# import cv2
# import numpy as np
#
# img = np.zeros((350, 350), dtype="uint8")
#
# circle = cv2.circle(img.copy(), (0, 0), 80, 255, -1)
# square = cv2.rectangle(img.copy(), (25, 25), (250, 250), 255, -1)
#
# img = cv2.bitwise_not(square)
#
# cv2.imshow("", img)
# cv2.waitKey(0)
import cv2
import imutils
import numpy as np

img = cv2.imread("39c904a01bea137cdb2d7d09f856e9f0.jpg")

img = cv2.resize(img, (1000, 800))

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_gray = cv2.bilateralFilter(img_gray, 5, 20, 20)
img_gray = cv2.Canny(img_gray, 50, 90)

kernal = np.ones((4, 4),dtype="uint8")
img_gray = cv2.dilate(img_gray, kernal,iterations=3)
img_gray = cv2.erode(img_gray,kernal,iterations=3)

# cv2.imshow("", img_gray)
# cv2.waitKey(0)

conture = cv2.findContours(img_gray, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
conture = imutils.grab_contours(conture)
conture = sorted(conture, key=cv2.contourArea, reverse=True)

pos = None
q = []
for i in conture:
    app = cv2.approxPolyDP(i, 80, True)
    print(f'{app=}')

    if len(app) <10:
        q.append(app)


mask = np.zeros(img_gray.shape, dtype="uint8")
for i in q:
    cv2.drawContours(mask, [i], -1, 255, -1)
bit = cv2.bitwise_and(img, img, mask=mask)
print(pos)
cv2.imshow("", bit)
cv2.waitKey(0)
