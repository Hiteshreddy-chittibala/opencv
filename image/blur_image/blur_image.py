import cv2

img = cv2.imread("/home/hiteshreddy/opencv/Meme God.jpg")

resized = cv2.resize(img, (500, 500))

blur = cv2.GaussianBlur(resized, (21,21), 0)

cv2.imwrite("blur_img.jpg",blur)

cv2.imshow("Image",blur)
cv2.waitKey(0)
cv2.destroyAllWindows()
