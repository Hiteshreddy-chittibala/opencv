from ultralytics import YOLO
import cv2

# Load your trained segmentation model
model = YOLO("/home/hiteshreddy/Tasks_on_AIML/segmentation/runs/segment/train-3/weights/best.pt")

video_path =("/home/hiteshreddy/opencv/video_1.mp4")

video = cv2.VideoCapture(video_path)

if not video.isOpened():
    print("Error: Could not find video.")
    exit()
width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(width, height)

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter("output_1.mp4", fourcc,20,(width,height))

while True:
    ret, frame = video.read()

    if not ret:
        break

    # Perform segmentation
    results = model.predict(
        source=frame,
        conf=0.5,
        verbose=False
    )

    # Draw segmentation masks and labels
    annotated_frame = results[0].plot()
    out.write(annotated_frame)
    display = cv2.resize(annotated_frame, (640,480))
    # Show result
    cv2.imshow("YOLOv8 Segmentation", annotated_frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video.release()
out.release()
cv2.destroyAllWindows()
print("video saved to local files")
