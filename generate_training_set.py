import imageio
import os
import glob
import random

import numpy as np
import pandas as pd
from PIL import Image

path = '/camp/lab/tedescos/home/users/chois1/computational_tools/yolov7/data/bf_migration/cell_therapy/cytokine_migration_trial_1/'
savepath = '/camp/lab/tedescos/home/users/chois1/computational_tools/yolov7/data/bf_migration/cell_therapy/cytokine_migration_trial_train_set_1/'

filenames = next(os.walk(path))[1]
imgtype = '.png'

for i in range(len(filenames)):
    dirname = path + filenames[i] + '/*.png'
    image_stack = glob.glob(dirname)
    rndm_img = random.choice(image_stack)
    
    imgname = os.path.split(rndm_img)[1].replace('.png', '')
    rndm_img = np.array(imageio.imread(rndm_img))
    imageio.imsave(savepath + imgname + imgtype, rndm_img)



