import cv2

video = cv2.VideoCapture(2)

# Get webcam frame width and height
width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(width, height)

#video codec means how video is compressed and stored beacause video meade many frame and it size becomes huge so it is used
#XVID is video code and xvid is to compress and store
#fourcc is four character code
save_video = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter("output_savedvideo.avi", save_video,20,(width, height))

while True:
    rat, frame = video.read()

    if not rat:
        print("No camera found")
        break
    out.write(frame)
    cv2.imshow("Type l to close window", frame)

    if cv2.waitKey(1) & 0xFF == ord('l'):
        break

video.release()
out.release()
cv2.destroyAllWindows()
