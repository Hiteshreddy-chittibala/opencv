import cv2

img = cv2.imread("/home/hiteshreddy/opencv/Meme God.jpg")

resized = cv2.resize(img,(500,500))
cv2.imshow("Image",resized)
cv2.imwrite("O_Image.jpg",resized)
cv2.waitKey(1000)

flip = cv2.flip(resized, 1)
cv2.imshow("Flipped",flip)
cv2.imwrite("Horizontal_flip.jpg",flip)
cv2.waitKey(2000)

flip1 = cv2.flip(flip, 0)
cv2.imshow("verti_Flipped",flip1)
cv2.imwrite("Vertical_flip.jpg",flip1)
cv2.waitKey(2000)

flip2 = cv2.flip(flip1, -1)
cv2.imshow("Original_Flipped",flip2)
cv2.imwrite("Original_flip.jpg",flip2)
cv2.waitKey(2000)

cv2.destroyAllWindows()

