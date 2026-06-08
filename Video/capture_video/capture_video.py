import cv2

cap = cv2.VideoCapture(2)

while True:
    ret, frame = cap.read()   #ret is frame is captured or not , frame is for actual image

    if not ret:
        print("Camera not found")
        break

    cv2.imshow("External Camera", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
