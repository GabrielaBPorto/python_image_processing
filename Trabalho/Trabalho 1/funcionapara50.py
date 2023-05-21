#!/usr/bin/python

import sys
import numpy as np
import operator

from PIL import Image

def calculaqtdPixel(imageSizeO, pixelSize):
	i = 1

	num = pixelSize
	resto = divmod(num, 1)

	while((resto[1] < 0.01 or resto[1] > 0.09) and resto[1] != 0.0):
		i = i + 1
		num = pixelSize*i
		resto = divmod(num, 1)

	return(int(num),i)


#Leitura da linha de comando

imageName = sys.argv[1]
porcentualAmostragem = float(sys.argv[2]) / 100
greylevels = int(sys.argv[3])
tecnica = sys.argv[4]

#Leitura da imagem
try:
    img = Image.open(imageName)
except:
    print("Unable to load image")


new_size = np.array(np.array(img.size, float) * (1-porcentualAmostragem), int)

try:
	newimage = Image.new(img.mode, new_size)
except:
	print("Unable to load new image")

qtdPixelO, qtdPixelD = calculaqtdPixel(img.size[0], (img.size[0]/ (new_size[0] *1.0)))
print(qtdPixelO, qtdPixelD)
print(img.size)
print(new_size)

temp = (0,0,0,0)


pixels = img.load()
newpixels = newimage.load()


janela = 2
print(janela)
temp = (0,0,0,0)
pixelLinha = 0

i = 0
u = 0
for a in range(new_size[0]):
	pixelColuna = 0
	for b in range(new_size[1]):
		for l in range(janela):
			for k in range(janela):
				temp = np.add(np.array(pixels[pixelLinha+l, pixelColuna+k]), temp)
		newpixels[a,b] = tuple(ta/(janela*janela) for ta in temp)
		temp = (0,0,0,0)
		print(pixelLinha,pixelColuna)
		pixelColuna = pixelColuna + 1
		i = i + 1
		if(i == qtdPixelD):
			pixelColuna = pixelColuna + janela
			i = 0
	pixelLinha = pixelLinha + 1
	if(pixelLinha > img.size[0]):
		break


newimage.show()
img.show()
exit()

#percorre a linha
for a in range(new_size[0]):
	for b in range(new_size[1]):
		#Trata a coluna que falta
		if(j >= img.size[1]-vezesc):
			valor = img.size[1]- j
			for l in range(vezesl):
				for k in range(valor):
					temp = tuple(np.add(np.array(pixels[i+l,j+k],int),temp))
			newpixels[a,b] = tuple(ta/(vezesl*valor) for ta in temp)
			temp = (0,0,0,0)
			j = 0
		else:
			for l in range(vezesl):
				for c in range(vezesc):
					temp =  tuple(np.add(np.array(pixels[i+l,j+c],int), temp))
			temp1 = tuple(ta/(vezesc*vezesl) for ta in temp)
			newpixels[a,b] = temp1
			temp = (0,0,0,0)
			j = j + vezesc
	#Trata a linha que falta
	if(i >= img.size[0]-vezesl):
		valor = img.size[0]- i
		for k in range(valor):
			for c in range(vezesc):
				temp = tuple(np.add(np.array(pixels[i,j+k],int), temp ))
		temp1 = tuple(ta/(valor) for ta in temp)
		newpixels[a,b] = temp1
		temp = (0,0,0,0)
		i = 0
	else:
		i = i + vezesl


# Quantizacao da amostragem

if tecnica == "media":
	for a in range(new_size[0]):
		for b in range(new_size[1]-(vezesc)):
			for l in range(vezesl):
				for c in range(vezesc):
					temp =  tuple(np.add(np.array(pixels[a+l,b+c],int), temp))	 
			temp1 = tuple(ta/vezesc*vezesl for ta in temp)
			newpixels[a,b] = temp1
			temp = (0,0,0,0)
		#Trata a coluna



newimage.show()
img.show()