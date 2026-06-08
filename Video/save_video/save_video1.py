import cv2

cap = cv2.VideoCapture(2)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

#mp4 codec
vedio = cv2.VideoWriter_fourcc(*'MP4v')

out = cv2.VideoWriter("video_output1.mp4", vedio, 20, (width, height))

while True:
    ret, frame = cap.read()

    if not ret:
        print("camera not found")
        break

    out.write(frame)

    cv2.imshow("press q to stop vedio", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()



