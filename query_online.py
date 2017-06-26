# -*- coding: utf-8 -*-
# Author: yongyuan.name

import numpy as np
import h5py

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

h5f = h5py.File('featsCNN.h5','r')
feats = h5f['dataset_1'][:]
imgNames = h5f['dataset_2'][:]
h5f.close()


queryVec = feats[2]
print "query shape:",queryVec.shape
scores = np.dot(queryVec, feats.T)

rank_ID = np.argsort(scores)[::-1]
rank_score = scores[rank_ID]
#print rank_ID
#print rank_score

maxres = 6
imlist = [imgNames[index] for i,index in enumerate(rank_ID[0:maxres])]
#print "name of images in the order of similarity" 
#print imlist

limit = 5 # number of top retrieved images to show
showlist = imlist[:limit]
 

for i,im in enumerate(showlist):
    image = mpimg.imread("database/"+im)
    plt.title("search output %d" %(i+1))
    plt.imshow(image)
    plt.show()
