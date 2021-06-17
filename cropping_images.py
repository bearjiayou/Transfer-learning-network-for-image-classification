# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 19:10:14 2021

@author: Ren Sijin
"""
#guss noise
import skimage
from skimage import io
import matplotlib.pyplot as plt
import os
import numpy as np
from PIL import Image

dire="G:/Thesis/original images/trail images/scaled image/"
list = os.listdir(dire) 
number_files=list
#rotate the images 
c=np.random.choice(number_files, 2000, replace = False)

# Setting the points for cropped image 
#the begin point
A=0.25
#the end point
B=0.75
C=0.25
D=0.75

count = 0
while (count < 2000):     
    
    count = count + 1
    i=count-1
    b=c[i]
    if os.path.exists(dire+b) is True: 
        im = Image.open(dire+b)
        width, height = im.size # the size is 150*150
        left=A*width
        right=B*width
        top=C*height
        bottom=D*height
        im1 = im.crop((left, top, right, bottom)) 
        im1.save(dire+'c'+b)
        os.remove(dire+b)
        
        