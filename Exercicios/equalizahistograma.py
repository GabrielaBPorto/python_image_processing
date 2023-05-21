import cv2
import sys
import numpy as np

imgName = sys.argv[1]

img = cv2.imread(imgName, 0)

eq = cv2.equalizeHist(img)# retorna uma imagem com histograma equalizado

res = np.hstack ((img,eq))# cria uma imagem com as duas imagens uma do lado da outra

cv2.imwrite('res.png', res)

cv2.namedWindow('image', cv2.WINDOW_NORMAL) # Normaliza o tamanho que aparece a janela

cv2.imshow('image', eq) #Nome da tela, imagem
cv2.waitKey(0)
cv2.destroyAllWindows()
