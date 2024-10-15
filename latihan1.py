# import cv2


# citra = cv2.imread("kampus-universitas-bsi-kaliabang_210322144150-542.jpeg")
# cv2.imshow("gedung bsi",citra)
# cv2.imshow("gedung bsi blue",citra[:,:,0])
# cv2.imshow("gedung bsi green",citra[:,:,1])
# cv2.imshow("gedung bsi red",citra[:,:,2])
# print (citra)
# print (citra[0,2,0])
# print (citra[:,:,1])
import cv2

# Membaca citra digital dari komputer
# citra = cv2.imread("kampus-universitas-bsi-kaliabang_210322144150-542.jpeg")
citra = cv2.imread("GY2Vf_RXAAAgsll.jfif")

# Menampilkan citra asli
cv2.imshow("Gedung BSI Asli", citra)

# Memisahkan channel warna dan menampilkannya
b, g, r = cv2.split(citra)
cv2.imshow("Gedung BSI Blue", b)
cv2.imshow("Gedung BSI Green", g)
cv2.imshow("Gedung BSI Red", r)

# Menggabungkan kembali channel warna untuk verifikasi
citra_gabungan = cv2.merge([b, g, r])
cv2.imshow("Gedung BSI Gabungan", citra_gabungan)

# Mencetak matriks dari citra BGR
print(citra)

# Menunggu sampai user menekan sembarang tombol
cv2.waitKey(0)
cv2.destroyAllWindows()