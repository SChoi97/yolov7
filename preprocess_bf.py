import sys
sys.path.append('/camp/lab/tedescos/home/users/chois1/computational_tools/yolov7/lib/python3.8/site-packages')

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import imageio
import os
import re
import tifffile

#-------------
# Functions
#-------------

def normalise(im):
  '''Function to normalise between [0, 1]'''
  max = np.max(im)
  min = np.min(im)
  norm = (im - min) / (max - min)

  return norm

numbers = re.compile(r'(\d+)')
def numericalSort(value):
    parts = numbers.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts

#paths
basepath = '/camp/lab/tedescos/home/users/chois1/Vale/'
experiment_path = '221017_ncrm5_1078_ipstoMyoblast_day5induction3/221017_ipstomyoblast_induction_day5_3/'

path = basepath + experiment_path
savepath = '/camp/lab/tedescos/home/users/chois1/computational_tools/yolov7/data/bf_migration/Vale/221017_ipstomyoblast_induction_day5/'

#----------------------
# Open .OME.TIF Files
#----------------------

images = []

for root, dirs, files in os.walk(path, topdown=False):
   for name in files:
    if 'tif' in os.path.join(root, name):
      filename = os.path.join(root, name)
      ome_stack = tifffile.imread(filename)
      
      '''
      Generate a folder to save normalised images - image stack gets a single folder of individual images.
      '''
      foldername = name.replace('.ome.tif', '')
      savedir = savepath + foldername + '_NORM'
      if not os.path.exists(savedir):
        os.mkdir(savedir)
    
      counter = 0
      for i in range(ome_stack.shape[0]):
        image = ome_stack[i]        
        norm_image = normalise(image)
        imageio.imsave(savedir + '/' + foldername + '_norm_time_point_' + str(counter) + '.png', norm_image)
        counter += 1
      


