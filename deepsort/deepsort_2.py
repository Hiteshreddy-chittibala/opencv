import cv2
from ultralytics import YOLO
from deep_sort_realtime.deepsort_tracker import DeepSort

# Load your trained model
model = YOLO("/home/hiteshreddy/yolov8_project/runs/detect/train-2/weights/best.pt")

# Initialize DeepSORT
tracker = DeepSort(max_age=30)

# Open video (use 0 for webcam)
cap = cv2.VideoCapture(0)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

video = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter("Video_2.mp4", video, 30, (width,height))

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Detect objects
    results = model(frame)[0]
    detections = []
    for box in results.boxes:
       
        # Bounding box
        x1, y1, x2, y2 = box.xyxy[0]
      
        # Confidence
        conf = float(box.conf[0])
      
         # Class
        cls = int(box.cls[0])
        label = model.names[cls]
         
        detections.append(
            (
                [float(x1),
                 float(y1),
                 float(x2 - x1),
                 float(y2 - y1)],
                conf,
                label
            )
        )
    
    # Update tracker
    tracks = tracker.update_tracks(
        detections,
        frame=frame
    )

    # Draw tracks
    for track in tracks:
        if not track.is_confirmed():
            continue
        track_id = track.track_id
        l, t, r, b = track.to_ltrb()

        # Get class name stored by DeepSORT
        class_name = track.get_det_class()
        cv2.rectangle(
            frame,
            (int(l), int(t)),
            (int(r), int(b)),
            (0,255,0),
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
    out.write(frame)
    resize = cv2.resize(frame, (640,480)) 
    cv2.imshow("Bottle & Cup Tracking", resize)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()

