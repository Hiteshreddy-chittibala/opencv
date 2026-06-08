import cv2
cap = cv2.VideoCapture(2)

count = 0

while count < 10:
    ret, frame = cap.read()

    if not ret:
        break

    cv2.imshow("Camera", frame)
    filename = f"image_{count}.jpg"
    cv2.imwrite(filename, frame)
    print(filename, "saved")
    count += 1
    cv2.waitKey(100)

cap.release()
cv2.destroyAllWindows()
