import cv2
import numpy as np

src = cv2.imread('kucing.jpg', 1)

# aplly averaging blur on src image
dst = cv2.blur(src,(5,5))

# display input and output image
cv2.imshow("Averaging Smoothing",np.hstack((src,dst)))
cv2.waitKey(0) # waits until a key is pressed
cv2.desroyAllwindows() # destoys the window showing images