
from ultralytics import YOLO
import cv2
import numpy as np

# Load YOLO model
model = YOLO("yolov8n.pt")

# Open cameras
cap = cv2.VideoCapture(0)
cap1 = cv2.VideoCapture(2)

while True:

    # -------- Camera 1 --------
    ret, frame = cap.read()

    if ret:
        # YOLO detection
        results = model(frame)

        # Draw detections
        annotated = results[0].plot()

    else:
        # Create black screen
        annotated = np.zeros((480, 640, 3), dtype=np.uint8)

        # Display error text
        cv2.putText(
            annotated,
            "Camera 1 Not Available",
            (50, 240),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 255),
            2
        )

    # -------- Camera 2 --------
    ret1, frame1 = cap1.read()

    if ret1:
        # YOLO detection
        results1 = model(frame1)

        # Draw detections
        annotated1 = results1[0].plot()

    else:
        # Create black screen
        annotated1 = np.zeros((480, 640, 3), dtype=np.uint8)

        # Display error text
        cv2.putText(
            annotated1,
            "Camera 2 Not Available",
            (50, 240),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 255),
            2
        )

    # Show windows
    cv2.imshow("Camera 1", annotated)
    cv2.imshow("Camera 2", annotated1)

    # Quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release cameras
cap.release()
cap1.release()

# Close windows
cv2.destroyAllWindows()

