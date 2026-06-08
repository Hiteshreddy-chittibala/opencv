import cv2
img = cv2.imread("/home/hiteshreddy/opencv/Meme God.jpg")

#it give size for image   width, height
resized = cv2.resize(img, (700,550))

cv2.imshow("Image", resized)
cv2.waitKey(0)
cv2.destoryAllWindows()
