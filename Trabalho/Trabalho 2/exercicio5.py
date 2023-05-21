#!/usr/bin/python

import cv2
import cv
import sys
import numpy as np

#Imagem principal
imgName = sys.argv[1]


try:
	img = cv2.imread(imgName)
except:
	print("Erro em carregar a imagem")


color = [(255,0,0),(0,255,0),(0,0,255)]
dic = ["hulk1.png","hulk2.png","iron1.png","iron2.png","k3po1.png","k3po2.png",
		"magneto1.png","magneto2.png","trooper1.png","trooper2.png","vader1.png",
		"vader2.png", "volve1.png", "volve2.png"]

print(len(dic))

#Cria matrizes onde sao guardadas as informacoes de comparacao de histograma
correl = np.zeros((14,3))
chisqr = np.zeros((14,3))
intersect = np.zeros((14,3))
bhattacharyya = np.zeros((14,3))



for i,j in enumerate(dic):
	name = j
	print("O nome is ", i, " e o outro e ", j)
	#Se o nome for diferente faz a comparacao, nao adianta comparar a imagem com a mesma
	if(imgName != name):
		try:
			img2 = cv2.imread(name)
		except:
			print("Erro em carregar a imagem")

		#Enche as listas de valor de comparacao entre a imagem principal e a imagem da vez
		for ch, col in enumerate(color):
			#Pega o hist decada tipo de cor e entao coloca nos seus tipos de comparacao
			hist_item1 = cv2.calcHist([img], [ch], None, [256], [0,255])
			hist_item2 = cv2.calcHist([img2], [ch], None, [256], [0,255])
			cv2.normalize(hist_item1, hist_item1, 0, 255, cv2.NORM_MINMAX)
			cv2.normalize(hist_item2, hist_item2, 0, 255, cv2.NORM_MINMAX)

			correl[i][ch] = (cv2.compareHist(hist_item1, hist_item2, cv.CV_COMP_CORREL))
			chisqr[i][ch] = (cv2.compareHist(hist_item1, hist_item2, cv.CV_COMP_CHISQR))
			intersect[i][ch] = (cv2.compareHist(hist_item1, hist_item2, cv.CV_COMP_INTERSECT))
			bhattacharyya[i][ch] = (cv2.compareHist(hist_item1, hist_item2, cv.CV_COMP_BHATTACHARYYA))

mina = 0
minb = 0

for i in range(3):
	for j in range(15):
		if(correl[i][j] < correl[mina][minb])
			mina = i, minb = j
