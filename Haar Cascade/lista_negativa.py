import urllib

import numpy as np

import cv2

import os



for file_type in ['negativas']:

    for img in os.listdir(file_type):

        if file_type == 'negativas':

            line = file_type+'/'+img+'\n'

            with open('bg.txt','a') as f:

                f.write(line)
