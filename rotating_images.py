# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 19:13:00 2021

@author: Ren Sijin
"""
import os
from PIL import Image
import numpy as np

n = 437
dire="C:/Data/sr2339/Thesis/rotated/45/test/buildings/"
list = os.listdir(dire) 
number_files=list

#choose the image
c=np.random.choice(number_files, n,replace=False)
#print(c)
#change the name of the chosen images

count = 0
while (count < n):     
    
    count = count + 1
    i=count-1
    b=c[i]
    
    if os.path.exists(dire+b) is True:
        catIm = Image.open(dire+b)
        rotate = catIm.rotate(45)
        rotate.save(dire+'o'+b, 'JPEG')
        os.remove(dire+b)
