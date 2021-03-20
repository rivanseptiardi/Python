import cv2

capture = cv2.VideoCapture(0)
while (True):

    _, frame = capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.blur(gray,(1,23))
    cv2.imshow('frame', blur)

    if cv2.waitKey(5000) & 0xFF == ord('q'):
        break

    capture.release()
    cv2.destroyAllWindows()
