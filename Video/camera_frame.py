import cv2

video = cv2.VideoCapture(2)
count = 0

while True:
    ret, frame = video.read()

    if not ret:
        break

    cv2.imshow("webcam", frame)
    
    key = cv2.waitKey(1)
    if key == ord('s'):
        filename = f'filename_{count}.jpg'
        cv2.imwrite(filename, frame)
        print(filename, 'saved')
        count += 1

    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
