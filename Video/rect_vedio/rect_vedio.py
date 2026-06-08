import cv2

cap = cv2.VideoCapture(2)
count  = 0
while True:
    ret, frame = cap.read()

    if not ret:
        break

    cv2.rectangle(frame, (100,100), (300,350), (0,255,0), 2)
    cv2.imshow("camera", frame)
    
    key = cv2.waitKey(1) & 0xFF
    if key == ord('s'):
        filename = f'image_{count}.jpg'
        cv2.imwrite(filename, frame)
        print(filename, "saved")
        count += 1

    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
