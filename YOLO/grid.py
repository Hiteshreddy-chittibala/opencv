from ultralytics import YOLO
import cv2
import numpy as np
model = YOLO('yolov8n.pt')
# Open cameras
cams = [
    cv2.VideoCapture(0),
    cv2.VideoCapture(1),
    cv2.VideoCapture(2),
    cv2.VideoCapture(3)
]
# Video codec
save_video = cv2.VideoWriter_fourcc(*'mp4v')
# Video writer
out = cv2.VideoWriter(
    'dashboard.mp4',
    save_video,
    20,
    (800, 600)
)
while True:
    frames = []
    for i, cam in enumerate(cams):
        ret, frame = cam.read()
        if ret:
            # YOLO detection
            results = model(frame)
            # Draw detections
            annotated = results[0].plot()
            # Resize frame
            annotated = cv2.resize(annotated, (400, 300))
        else:
            # Black screen
            annotated = np.zeros((300, 400, 3), dtype=np.uint8)
            cv2.putText(
                annotated,
                f"Camera {i} Not Available",
                (20, 150),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 0, 255),
                2
            )
        frames.append(annotated)
    # Top row
    top = np.hstack((frames[0], frames[1]))
    # Bottom row
    bottom = np.hstack((frames[2], frames[3]))
    # Final dashboard
    dashboard = np.vstack((top, bottom))
    # Save dashboard video
    out.write(dashboard)
    # Show dashboard
    cv2.imshow("All Cameras", dashboard)
    # Quit
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
# Release cameras
#for cam in cams:
    cam.release()
# Release video writer
out.release()
cv2.destroyAllWindows()
