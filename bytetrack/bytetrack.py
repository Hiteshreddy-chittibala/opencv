import cv2
from ultralytics import YOLO

model = YOLO("yolov8n.pt")

video = cv2.VideoCapture("/home/hiteshreddy/opencv/video.mp4")
width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(width, height)

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter("output.mp4", fourcc,20,(width, height))

while True:
    ret, frame = video.read()
    if not ret:
        print("Video has completed")
        break

    # Detect and track objects
    results = model.track(
        source=frame,
        persist=True,
        tracker="bytetrack.yaml"
    )

    annotated_frame = results[0].plot()
    out.write(annotated_frame)
    display = cv2.resize(annotated_frame, (640,480))
    cv2.imshow("YOLO + ByteTrack", annotated_frame)

    # Exit on 'q'
    if cv2.waitKey(10) & 0xFF == ord("q"):
        break

video.release()
out.release()
cv2.destroyAllWindows()
print("Video saved successfully")
