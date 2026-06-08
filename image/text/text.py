import cv2

pic = cv2.imread("/home/hiteshreddy/opencv/Meme God.jpg")
size = cv2.resize(pic, (500,500))

#path name, text, position(x,y),Font Type, Font size, color,Thickness
cv2.putText(size, 
          "MEME GOD",
          (50,100), 
          cv2.FONT_HERSHEY_TRIPLEX | cv2.FONT_ITALIC, 
          1, 
          (0,255,0), 
          2) 
cv2.imshow("Picture",size)
cv2.imwrite("Text_pic.jpg",size)

cv2.waitKey(0)
cv2.destroyAllWindows()

