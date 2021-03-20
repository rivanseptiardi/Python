import cv2
import numpy

# read image
src = cv2.imread('kucing.jpg', cv2.IMREAD_UNCHANGED)

# aplly averaging blur on src image
dst = cv2.GaussianBlur(src,(7,7),0)

# display input and output image
cv2.imshow("Gaussian Smoothing",numpy.hstack((src,dst)))
cv2.waitKey(0) # waits until a key is pressed
cv2.desroyAllwindows() # destoys the window showing image