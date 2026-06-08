import cv2

video = cv2.VideoCapture("/home/hiteshreddy/opencv/video.mp4")

count = 0
while True:
    ret, frame = video.read()

    if not ret:
        break

    filename = f"frame{count}.jpg"
    cv2.imwrite(filename, frame)
    print(filename, "saved")

    count +=1

video.release()
cv2.destroyAllWindows()
