import cv2

video = cv2.VideoCapture(2)

while True:
    ret, frame = video.read()

    if not ret:
        print("camera is not working")
        break

    cv2.imshow("external_camera",frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):

        cv2.imwrite("captured_img.jpg", frame)
        print("image saved")
        break

video.release()

cv2.destroyAllWindows()
