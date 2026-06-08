import cv2

video = cv2.VideoCapture(2)
count =0
while True:
    ret, frame = video.read()

    if not ret:
        break

    #rotate = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
    center = (450,350)
    matrix = cv2.getRotationMatrix2D(center, 150, 1)
    rotated = cv2.warpAffine(frame, matrix, (900,700))
    cv2.imshow("roated", rotated)

    key = cv2.waitKey(1)
    if  key == ord('s'):
        filename = f'file_{count}.jpg'
        cv2.imwrite(filename, rotated)
        print(filename, "saved")
        count += 1

    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
