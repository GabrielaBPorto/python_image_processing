#Equalizacao local
import cv2
import sys
import numpy as np
from matplotlib import pyplot as plt

imgName = sys.argv[1]
img = cv2.imread(imgName,0)

# create a CLAHE object (Arguments are optional).
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl1 = clahe.apply(img)

cv2.imwrite('clahe_2.jpg',cl1)