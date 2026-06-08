import cv2

pic = cv2.imread("/home/hiteshreddy/opencv/Meme God.jpg")

crop = pic[300:600, 400:700]   #y1:y2, x1:x2  y1=start height, y2= stop height & x1=start width , x2= stop widht
crop1 = pic[0:500, 0: 550]
cv2.imshow("Original", pic)
cv2.waitKey(1000)
print(pic.shape)
cv2.imshow("crop_img", crop)
print(crop.shape)
cv2.waitKey(1000)  
cv2.imshow("crop1_img", crop1)
cv2.waitKey(10000)
cv2.destroyAllWindows()
