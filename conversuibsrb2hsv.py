import cv2

img = cv2.imread("GY2Vf_RXAAAgsll.jfif")

hsv_img = cv2.cvtColor(img,cv2.COLOR_RGB2HSV)

cv2.imshow('gambar',img)
cv2.imshow('gambar hsv',hsv_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
