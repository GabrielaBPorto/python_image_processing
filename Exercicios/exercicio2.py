import cv2
import sys	
import numpy as np
import math
import matplotlib.pyplot as plt

imgName= sys.argv[1]
 
img = cv2.imread(imgName)

h = np.zeros((300,256,3))

t = []

bins = np.arange(256).reshape(256,1)
color = [ (255,0,0),(0,255,0),(0,0,255) ]
for ch, col in enumerate(color):
	hist_item = cv2.calcHist([img],[ch],None,[256],[0,256])
	t.append(hist_item)
	# cv2.normalize(hist_item,hist_item,0,255,cv2.NORM_MINMAX)
	hist = np.int32(np.around(hist_item))
	pts = np.column_stack((bins,hist))
	cv2.polylines(h,[pts],False,col)
 
h= np.flipud(h)


plt.plot(hist, hist, "r")
plt.show()

# cv2.imshow('colorhist',h)
# cv2.waitKey(0)