import cv2
import sys
import numpy as np
from matplotlib import pyplot as plt


imgName = sys.argv[1]

img = cv2.imread(imgName)

eq = cv2.equalizeHist(img)
# retorna uma imagem com histograma equalizado


color = ('b','g','r')
for i,col in enumerate(color):
	hist = cv2.calcHist(eq.flatten(),[i],None,[256],[0,256])
	plt.plot(hist,color = col)


plt.xlim([0,256])
plt.show()



res = np.hstack ((img,eq))# cria uma imagem com as duas imagens uma do lado da outra
cv2.imshow('imagem', res)
cv2.waitKey(0)
cv2.destroyAllWindows()


# cv2.imwrite('res.png', res)