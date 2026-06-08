import cv2
img = cv2.imread("/home/hiteshreddy/opencv/Meme God.jpg")
cv2.imshow("Image",img)    #Image is a window_name to open the image
cv2.waitKey(0)
cv2.destroyAllWindows()  #it says clean the os and shut window and make space free because in .imshow() is created the window handled by os
