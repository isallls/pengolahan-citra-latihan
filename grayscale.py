import cv2 

img = cv2.imread('GY2Vf_RXAAAgsll.jfif')

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY);
grays = cv2.cvtColor(img,cv2.COLOR_BGR2RGB);
cv2.imshow('Gambar Asli ',img)
cv2.imshow('gambar gray', gray)
# cv2.imshow('gambar gray', grays)
cv2.waitKey()