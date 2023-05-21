#!/usr/bin/python

import cv2
import cv
import sys
import numpy as np


color = [(255,0,0),(0,255,0),(0,0,255)]

dic = zip(range(14), ["hulk1.png","hulk2.png","iron1.png","iron2.png","k3po1.png","k3po2.png",
		"magneto1.png","magneto2.png","trooper1.png","trooper2.png","vader1.png",
		"vader2.png", "volve1.png", "volve2.png"])

def calculaHistograma(dicionario, color):
	#Cria matrizes onde sao guardadas as informacoes de comparacao de histograma
	correl = np.zeros((len(dicionario),3))
	chisqr = np.zeros((len(dicionario),3))
	intersect = np.zeros((len(dicionario),3))
	bhattacharyya = np.zeros((len(dicionario),3))


	#Calcula os histogramas
	for i,j in dicionario:
		name = j
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
	return(correl,chisqr,intersect,bhattacharyya)

def list_duplicates(seq):
  seen = set()
  seen_add = seen.add
  # adds all elements it doesn't know yet to seen and all other to seen_twice
  seen_twice = set(x for x in seq if x in seen or seen_add(x) )
  # turn the set into a list (as requested)
  return list(seen_twice)

def comparaMin(matriz, dicionario):
	mina, minb = 0,0
	mins = []
	imagens = []
	imagesqtt = 4
	#Histogramas sao comparados para saber qual sao os mais proximos a imagem base
	for k in range(imagesqtt):
		for i in range(3):
			for j in range(len(dicionario)):
				if(matriz[j][i] < matriz[mina][i]):
					mina = j
			mins.append(mina)
			mina = 0
		lista = list_duplicates(mins) # aqui recebemos o valor 11
		#retira essa imagem de dentro da matriz pra que nao caia nela novamente ?
		print(lista)
		# for b in range(len(lista)):
		for a in range(3):
			matriz[lista[0]][a] = 20000000

	return(lista)

def comparaMax(matriz,dicionario):
	a = []
	return(a)

def comparaInter(matriz,dicionario):
	a = []
	return(a)

def imprimeImage(lista, idbase, base):
	#Corrige o valor da imagem caso necessario
	imagens = []
	for i in lista:
		#Por que como a imagem estao lado a lado no dicionario e nao e feito comparacao da mesma 
		if(i == idbase):
			imagens.append(dic[i+1][1])
		else:
			imagens.append(dic[i][1])

	#Mostra as imagens
	cv2.imshow('base', base)

	cv2.waitKey(0)

	for i in imagens:
		print(i)
		try:
			img2 = cv2.imread(i)
		except:
			print("Erro em abrir a imagem")
		cv2.imshow('imagem', img2)
		cv2.waitKey(0)

	cv2.destroyAllWindows()


#Imagem principal
imgName = sys.argv[1]

try:
	img = cv2.imread(imgName)
except:
	print("Erro em carregar a imagem")

for i,j in dic:
	if(j == imgName):
		imgId = i

correl, chisqr, intersect, bhattacharyya = calculaHistograma(dic,color)	

listachisqr = comparaMin(chisqr, dic)
listabhatta = comparaMin(bhattacharyya, dic)
listacorrel = comparaMax(correl, dic)
listaintersect = comparaInter(intersect, dic)

imprimeImage(listachisqr, imgId, img)
imprimeImage(listabhatta, imgId, img)
