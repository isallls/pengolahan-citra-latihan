import cv2
import numpy as np  
from matplotlib import pyplot as plt 

img = cv2.imread("kampus-universitas-bsi-kaliabang_210322144150-542.jpeg",0)
plt.hist(img.ravel(),256,[0,256])
plt.show

