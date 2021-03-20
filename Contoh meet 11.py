# Tutorial Part 1

import cv2 #import library opencv

img = cv2.imread('1.jpg') #syntax open untuk membaca image pada folder
cv2.imshow('frame', img) #buka image pada window1
cv2.waitKey(0) #mennunggu event dari use untuk close window1
cv2.destroyAllWindows() #exit windows

import cv2
# akses webcam pada device anda, apabila anda menggunakan
# kamera eksternal pada laptop maka parameter VideoCapture diubah menjadi 1.
# namun apabila merupakan webcam bawaan parameter adalah 0.

capture = cv2.VideoCapture(0)

while(True):
    # fungsi kode dibawah untuk tangkap setiap frame pada webcam

    # perhatikan pada kode di bawah ada dua variabel yang memuat hasil dari
    # capture.read(). hal ini dikarenakan fungsi ini akan mereturn dua variabel
    # variabel pertama berupa boolean untuk memberi tahu bahwa frame terbaca atau belum
    # variabel kedua adalah frame itu sendiri

    _ , frame = capture.read()

    # ubah warna pada frame yang di tangkap menjadi HSV
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # tampilkan frame yang ditangkap kamera
    cv2.imshow('frame', gray)

    #tidak begitu penting, hanya berupa fungsi untuk keluar dari window
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# exit window dan matikan kamera
capture.release()
cv2.waitKey(0)
cv2.destroyAllWindows()