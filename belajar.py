# import library open cv
import cv2

# laad iamge (simpan image dalam 1 folder dengan source code)
img =  cv2.imread('logo.png', 1)
# tampilkan dalam 1 windows utama
cv2.imshow('gambar saya ', img)
# tunggu action dari user
cv2.waitKey(0)
#hapus semua windows (form) yag ada
cv2.destroyAllWindows()