import cv2
from ultralytics import YOLO
from deep_sort_realtime.deepsort_tracker import DeepSort

# -----------------------------
# Load your trained YOLO model
# -----------------------------
model = YOLO("/home/hiteshreddy/yolov8_project/runs/detect/train-2/weights/best.pt")

# -----------------------------
# Initialize DeepSORT
# -----------------------------
tracker = DeepSort(max_age=30)

# -----------------------------
# Open Video
# -----------------------------
cap = cv2.VideoCapture("/home/hiteshreddy/opencv/video_1.mp4")

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

out = cv2.VideoWriter(
    "output.mp4",
    cv2.VideoWriter_fourcc(*'mp4v'),
    fps,
    (width, height)
)

while True:

    ret, frame = cap.read()

    if not ret:
        break

    # -----------------------------
    # Run YOLO
    # -----------------------------
    results = model(frame)[0]

    detections = []

    # -----------------------------
    # Convert YOLO detections to DeepSORT format
    # -----------------------------
    for box in results.boxes:

        x1, y1, x2, y2 = box.xyxy[0]

        conf = float(box.conf[0])

        cls = int(box.cls[0])

        class_name = model.names[cls]

        detections.append(
            (
                [
                    float(x1),
                    float(y1),
                    float(x2 - x1),
                    float(y2 - y1)
                ],
                conf,
                class_name
            )
        )

    # -----------------------------
    # DeepSORT Tracking
    # -----------------------------
    tracks = tracker.update_tracks(
        detections,
        frame=frame
    )

    # -----------------------------
    # Draw Tracking Results
    # -----------------------------
    for track in tracks:

        if not track.is_confirmed():
            continue

        track_id = track.track_id

        l, t, r, b = track.to_ltrb()

        class_name = track.get_det_class()

        cv2.rectangle(
            frame,
            (int(l), int(t)),
            (int(r), int(b)),
            (0, 255, 0),
            2
        )

        cv2.putText(
            frame,
            f"{class_name} ID:{track_id}",
            (int(l), int(t)-10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0,255,0),
            2
        )

    # -----------------------------
    # Save and Display
    # -----------------------------
    out.write(frame)

    display = cv2.resize(frame, (640,480))
    cv2.imshow("DeepSORT Tracking", display)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
