import cv2

cap = cv2.VideoCapture(2)
count = 0
while True:
    ret, frame = cap.read()

    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edge = cv2.Canny(gray, 100, 200)
    cv2.imshow("edge_detection", edge)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('s'):
        filename = f'image_{count}.jpg'
        cv2.imwrite("edge_detection.jpg", edge)
        count += 1

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
