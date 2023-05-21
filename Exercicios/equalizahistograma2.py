import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt


imgName = sys.argv[1]

img = cv2.imread(imgName)
hist = cv2.calcHist([img], [0], None, [256], [0,256])



total = 0
#Pega a quantidade total de pixels na imagem
for i in hist:
	total = total + i

for i in len(hist):
	print()

plt.xlim([0,256])
plt.plot(hist, "r")
plt.show()