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

print(new_size)

temp = (0,0,0,0)


pixels = img.load()
newpixels = newimage.load()


janela = int((porcentualAmostragem*10) + 1)
print(janela)
temp = (0,0,0,0)
pixelLinha = 0
for a in range(new_size[0]):
	pixelColuna = 0
	for b in range(new_size[1]):
		for l in range(janela):
			for k in range(janela):
				temp = np.add(np.array(pixels[pixelLinha+l, pixelColuna+k]), temp)
		newpixels[a,b] = tuple(ta/(janela*janela) for ta in temp)
		temp = (0,0,0,0)
		pixelColuna = pixelColuna + 1
		# print(pixelLinha, pixelColuna)
		if(pixelColuna + janela > new_size[1]):
			u  = 1
	pixelLinha = pixelLinha + 1


newimage.show()
img.show()

exit()
