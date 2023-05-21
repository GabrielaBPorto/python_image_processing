#Equalizacao total
import cv2
import sys
import numpy as np
from matplotlib import pyplot as plt

imgName = sys.argv[1]
img = cv2.imread(imgName,0)
equ = cv2.equalizeHist(img)
res = np.hstack((img,equ)) #stacking images side-by-side
cv2.imwrite('res.png',res)