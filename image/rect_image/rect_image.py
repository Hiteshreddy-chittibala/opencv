import cv2

img = cv2.imread("/home/hiteshreddy/opencv/Meme God.jpg")
resized = cv2.resize(img, (500,500))

cv2.rectangle(resized,(200,200), (300,300), (0,160,0), 10) #topleft corner, bottomright corner, color, thickness
cv2.imshow("Image", resized)
cv2.imwrite("rect.jpg",resized)
cv2.waitKey(10000)
cv2.destroyAllWindows()
