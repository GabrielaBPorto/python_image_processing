import sys
import cv2
import numpy as np 
import imageshistogram


imageName = sys.argv[1]
queryimage = cv2.imread(imageName)