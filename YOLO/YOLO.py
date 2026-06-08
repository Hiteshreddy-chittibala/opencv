from ultralytics import YOLO
import cv2

#load yolo model
model = YOLO("yolov8n.pt")

#load camera
cap = cv2.VideoCapture(2)

#open camera
cam_available = cap.isOpened()

#check camera
if not cam_available:
    print("webcam is not available")
    exit()


while True:

    #camera
    if cam_available:
        ret, frame = cap.read()

        results = model(frame)

        annonated = results[0].plot()
        cv2.imshow("camera 1 window", annonated)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
