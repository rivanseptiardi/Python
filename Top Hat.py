import cv2
import numpy as np

img = cv2.imread('j.png', 0)
kernel = np.ones((5, 5), np.uint8)
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)

cv2.imshow("Tophat", np.hstack((img, tophat)))
cv2.waitKey(0)
cv2.destroyAllWindows()
