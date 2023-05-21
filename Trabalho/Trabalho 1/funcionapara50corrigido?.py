#!/usr/bin/python

import sys
import numpy as np
import operator

from PIL import Image


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

vezesl = img.size[0] /(new_size[0])
vezesc = img.size[1] / (new_size[1])
print(img.size)
print(vezesl, vezesc, new_size)
temp = (0,0,0,0)


pixels = img.load()
newpixels = newimage.load()

i = 0
j = 0
#percorre a linha
for a in range(new_size[0]):
	for b in range(new_size[1]):
		#Trata a coluna que falta
		if(j >= img.size[1]-vezesc):
			valor = img.size[1]- j
			for l in range(vezesl):
				for k in range(valor):
					temp = tuple(np.add(np.array(pixels[i+l,j+k],int),temp))
			temp1 = tuple(ta/(vezesl*valor) for ta in temp)
			newpixels[a,b] = temp1
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



newimage.show()
img.show()