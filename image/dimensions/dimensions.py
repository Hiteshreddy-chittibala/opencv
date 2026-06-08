import cv2

pic = cv2.imread("/home/hiteshreddy/opencv/Meme God.jpg")
size = cv2.resize(pic, (500,500))
h, w, c = size.shape
print(f"height = {h}, weidth = {w},channel = {c}")
