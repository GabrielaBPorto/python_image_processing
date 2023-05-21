#Gera 3 histogramas um para cada cor
import cv2
import sys
import numpy as np
from matplotlib import pyplot as plt

imgName = sys.argv[1]
img = cv2.imread(imgName)


color = ('b','g','r')
for i,col in enumerate(color):
	histr = cv2.calcHist([img],[i],None,[256],[0,256])
	plt.plot(histr,color = col)


plt.xlim([0,256])
plt.show()

#plota um histograma, mais visivel, mas só mostra tons de cinza

# plt.hist(img.ravel(), 256, [0,256]);
# plt.show()