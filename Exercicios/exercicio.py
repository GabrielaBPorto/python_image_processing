import cv2
import sys
from matplotlib import pyplot as plt
import numpy as np

imgName= sys.argv[1]

try:
	img = cv2.imread(imgName,0)
except:
	print("Erro em abrir a imagem")


#calcula histograma
histo = cv2.calcHist([img],[1],None, [256], [0,256])

t = np.arange(histo, histo1, histo2)

plt.plot(t, t,'b', t, t**2, 'r')
plt.xlim([0, 255])
plt.show()
