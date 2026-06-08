import cv2
import numpy as np
'''
np.zeros() creates an array filled with zeros.
np.zeros(shape, datatype)
'''
img = np.zeros((500,500,3), dtype="uint8")

pts = np.array([[20,30],      
                [300,200],
                [300,300],
                [200,300]], np.int32)   #np.int32 = 32-bit integer values


'''
pts = np.array([[100,100],
                [100,250],
                [300,250],
                [200,300]], np.int32)
'''
#cv2.polylines(image, points, isClosed, color, thickness)
cv2.polylines(img, [pts], True, (0,255,0), 3)

cv2.imshow("Polyline", img)
cv2.imwrite("polyline.jpg", img)
#cv2.imwrite("polyline1.jpg", img)

print("saved")
cv2.waitKey(0)
cv2.destroyAllWindows()
