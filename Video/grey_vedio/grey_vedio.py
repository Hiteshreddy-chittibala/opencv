import cv2 as cv
cap1 = cv.VideoCapture(0)
cap = cv.VideoCapture(2)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    ret1,frame1 = cap1.read()

    size = cv.resize(frame,(200,200))
    size1 = cv.resize(frame1,(200,200))
    # Our operations on the frame come here
    gray = cv.cvtColor(size, cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(size,(21,21), 0)
    # Display the resulting frame
    cv.imshow("frame1",size)
    cv.imshow("2nd frame",size1)
    cv.imshow('frame', gray)
    cv.imshow("frame2", blur)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv.destroyAllWindows()
