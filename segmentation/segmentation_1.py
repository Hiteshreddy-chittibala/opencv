from ultralytics import YOLO

model = YOLO("/home/hiteshreddy/Tasks_on_AIML/segmentation/runs/segment/train-3/weights/best.pt")

results = model.predict(
    source="/home/hiteshreddy/opencv/basic/openCV/segmentation/images/img_3.jpg",
    conf=0.5,
    save=True
)

print("Done!")
