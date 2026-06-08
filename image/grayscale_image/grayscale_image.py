import cv2

img_gray = cv2.imread("/home/hiteshreddy/opencv/Meme God.jpg",1)
img_gray1 = cv2.imread("/home/hiteshreddy/opencv/Meme God.jpg",0)
resized = cv2.resize(img_gray,(500,500))
resized1 = cv2.resize(img_gray1,(500,500))

cv2.imshow("Image", resized)
cv2.imwrite("resized1.jpg",resized)
cv2.waitKey(3000)

cv2.imshow("Image1", resized1)
cv2.imwrite("resized2.jpg",resized1)
cv2.waitKey(5000)


img = cv2.imread("/home/hiteshreddy/opencv/Meme God.jpg")
resized2 = cv2.resize(img,(500,500))
gray = cv2.cvtColor(resized2,cv2.COLOR_RGB2GRAY)
cv2.imshow("grayscale",gray)
cv2.imwrite("Grayscale_image.jpg",gray)
cv2.waitKey(3000)
cv2.destroyAllWindows()

