import cv2

img = cv2.imread("/home/hiteshreddy/opencv/Meme God.jpg")
resize = cv2.resize(img, (500,500))
rotate1 = cv2.rotate(resize, cv2.ROTATE_90_CLOCKWISE)
cv2.imshow("rotated",rotate1)
cv2.waitKey(1000)

rotate2 = cv2.rotate(resize, cv2.ROTATE_180)
cv2.imshow("rotated_180", rotate2)
cv2.waitKey(1000)


center = (250,250)   #it takes center of the image size
# Create rotation matrix
matrix = cv2.getRotationMatrix2D(center, 250, 1)   #center of image ,  degree of angle next size zoom in or out 1 is normalsize

# Rotate image
rotated = cv2.warpAffine(resize, matrix, (500,500))  #This is the function that actually applies the transformation.
cv2.imshow("rotated_250", rotated)
cv2.waitKey(1000)

center1 = (251,251)
matrix1 = cv2.getRotationMatrix2D(center1, 300, 2)
rotated1 = cv2.warpAffine(resize, matrix1, (500,500))
cv2.imshow("rotated_300", rotated1)
cv2.waitKey(1000)

cv2.destroyAllWindows()
