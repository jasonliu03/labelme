#!usr/bin/python
# -*- coding:utf-8 -*-
import PIL.Image
import numpy as np
from skimage import io,data,color
import matplotlib.pyplot as plt

import sys, os

def main():
    imgName = sys.argv[1] 
    path = os.path.dirname(imgName)
    print imgName, path
    img = PIL.Image.open(imgName)
    img = np.array(img)
    #dst = color.label2rgb(img, tongue_label=1, tongue_color=(255, 0, 255))
    DEFAULT_COLORS = ('red', 'magenta', 'blue', 'yellow', 'green',
                      'indigo', 'darkorange', 'cyan', 'pink', 'yellowgreen')
    dst = color.label2rgb(img, colors = DEFAULT_COLORS)
    io.imsave(path + '/label_2.png', dst)

if __name__ == '__main__':
    main()
