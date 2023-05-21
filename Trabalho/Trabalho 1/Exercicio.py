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


new_size = np.array(np.array(img.size, float) * porcentualAmostragem, int)
print(img.size)
print(new_size)


try:
	newimage = Image.new(img.mode, new_size)
except:
	print("Unable to load new image")

temp = (0,0,0,0)

vezesl = 4
vezesc = 4

pixels = img.load()
newpixels = newimage.load()

i = 0
#percorre a linha
for a in range(new_size[0]):
	j = 0
	jfinal = j+vezesc	
	for b in range(new_size[1]):
		for l in range(vezesl):
			for c in range(vezesc):
				temp = tuple(np.add(np.array(pixels[i+l,j+c],int),temp))
		temp1 = tuple(ta/(vezesl*vezesc) for ta in temp)
		newpixels[a,b] = temp1
		temp = (0,0,0,0)
		#Trata a coluna que falta
		j = j + vezesc
		if(jfinal == img.size[1]-1):
			print("O valor de j is %d e o valor de b is %d" %(j,b))

	#Trata a linha que falta
	if(i+vezesl > img.size[0]-1): # - vezes l?
		print("Trata linha final")


newimage.show()
# img.show()