import cv2 as cv

pic = cv.imread("/home/hiteshreddy/opencv/Meme God.jpg")

size = cv.resize(pic, (650,650))
cv.circle(size, (325,325), 100  , (0,255,0), 2)
cv.imshow("Circle_image", size)
cv.imwrite("Circle_image.jpg", size)
cv.waitKey(0)
cv.destroyAllWindows()
