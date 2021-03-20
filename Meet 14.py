import cv2
# Opening image
img = cv2.imread("image.jpg")
# OpenCV opens images as BRG
# but we want it as RGB and
# we also need a grayscale
# version
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# Creates the environment
# of the picture and shows it
cv2.imshow("Stop Sign", img_rgb)
cv2.waitKey(0)  # waits until a key is pressed
cv2.destroyAllWindows()  # destroys the window showing image