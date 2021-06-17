# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 18:59:11 2021

@author: Ren Sijin
"""

#import model to add noise
import cv2
import numpy as np
from skimage.util import random_noise
#import model to save,move images
import os
from PIL import Image

dire="C:/Data/sr2339/Thesis/noised/0.05/test/buildings"
list = os.listdir(dire) 
number_files=list
#rotate the images 
c=np.random.choice(number_files, 2000)

count = 0
while (count < 100):     
    
    count = count + 1
    i=count-1
    b=c[i]
    if os.path.exists(dire+b) is True: 
        img = cv2.imread(dire+b)
        noise_img = random_noise(img, mode='gaussian',var=0.1)
        noise_img = np.array(255*noise_img, dtype = 'uint8')
        new_im = Image.fromarray(noise_img)
        new_im.save(dire+'n'+b)
        os.remove(dire+b)