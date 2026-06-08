import cv2

img = cv2.imread("/home/hiteshreddy/opencv/Meme God.jpg")

cv2.imwrite("memeGod.jpg", img)
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
