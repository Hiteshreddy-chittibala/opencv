
from ultralytics import YOLO
import cv2
import numpy as np


# Load YOLO model
model = YOLO('yolov8n.pt')

# Open 4 cameras
cams =[
        cv2.VideoCapture(0),
        #cv2.VideoCapture(1),
        #cv2.VideoCapture(2),
        #cv2.VideoCapture(3)
    ]

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.mp4',
                      fourcc,
                      20.0,
                      (800,600)
                      )

while True:
    # Loop through cameras
    for i, cam in enumerate(cams):
        ret, frame = cam.read()

         # If camera works
        if ret:
            # Run YOLO detection
            results = model(frame)

            # Draw detections
            annonated = results[0].plot()

        else:

            # Create black screen
            annonated = np.zeros((500,500,3), dtype=np.uint8)  

            # Display error message
            cv2.putText(
                    annonated,
                    f"Camera {i} Not Available",
                    (50,240),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0,0,255),
                    3)
        # Resize all frames same size
        annonated = cv2.resize(annonated, (500, 500))

        out.write(annonated)
        # Show output
        cv2.imshow(f"Camera {i}", annonated)
    
    # Quit when Q pressed   
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release all cameras
for cam in cams:
    cam.release()
out.release()
# Close all windows
cv2.destroyAllWindows()
