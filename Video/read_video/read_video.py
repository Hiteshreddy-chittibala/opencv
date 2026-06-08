import cv2

video = cv2.VideoCapture("/home/hiteshreddy/video.mp4")

while True:
    ret, frame = video.read()

    if not ret:  #if video complete video stops
        print("video has completed")
        break
    
    #frame = cv2.resize(frame, (700, 450))

    cv2.imshow("video",frame)

    #0xFF it removes extra bit and uses only last 8 bits 
    #ex: i got 10000113 here we need last digts only so it takes 113
    #it say take clean key 
    if cv2.waitKey(10) & 0xFF == ord("q"): #0xFF means it is 255
        break
video.release()
cv2.destroyAllWindows()
