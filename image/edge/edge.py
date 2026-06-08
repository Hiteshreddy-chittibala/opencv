import cv2

img = cv2.imread("/home/hiteshreddy/opencv/road.jpg")

img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
size = cv2.resize(img_grey, (500,500))
edge = cv2.Canny(size, 50,100)   #edges = cv2.Canny(image, threshold1, threshold2)
cv2.imshow('image', edge)
cv2.imwrite("edge_img.jpg", edge)

cv2.waitKey(0)
cv2.destroyAllWindows()
