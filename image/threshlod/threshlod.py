import cv2

img = cv2.imread("/home/hiteshreddy/opencv/img.jpg")
imgg = cv2.resize(img, (300,300))
ret, thresh = cv2.threshold(imgg, 127, 255, cv2.THRESH_BINARY)
cv2.imshow("window", thresh)
cv2.waitKey(0)

ret1, thresh1 = cv2.threshold(imgg, 127, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("window1", thresh1)
cv2.waitKey(0)

ret2, thresh2 = cv2.threshold(imgg, 127, 255, cv2.THRESH_TRUNC)
cv2.imshow("window2", thresh2)
cv2.waitKey(0)

ret3, thresh3 = cv2.threshold(imgg, 127, 255, cv2.THRESH_TOZERO)
cv2.imshow("window3", thresh3)
cv2.waitKey(0)

ret4, thresh4 = cv2.threshold(imgg, 127, 255, cv2.THRESH_TOZERO_INV)
cv2.imshow("window4", thresh4)
cv2.waitKey(0)



cv2.destroyAllWindows()
