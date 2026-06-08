import cv2

#img = cv2.imread("/home/hiteshreddy/opencv/Meme God.jpg",cv2.IMREAD_GRAYSCALE)
img = cv2.imread("/home/hiteshreddy/opencv/Meme God.jpg",0)
cv2.imshow("Gray Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
