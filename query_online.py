# -*- coding: utf-8 -*-
# Author: yongyuan.name
from extract_cnn_vgg16_keras import VGGNet

import numpy as np
import h5py

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-query", required=True,
                help="Path to query which contains image to be queried")
ap.add_argument("-index", required=True,
                help="Path to index")
ap.add_argument("-result", required=True,
                help="Path for output retrieved images")
args = vars(ap.parse_args())

# read in indexed images' feature vectors and corresponding image names
with h5py.File(args["index"], 'r') as h5f:
    feats = h5f['dataset_1'][:]
    imgNames = h5f['dataset_2'][:]

print("--------------------------------------------------")
print("               searching starts")
print("--------------------------------------------------")

# read and show query image
queryDir = args["query"]
queryImg = mpimg.imread(queryDir)
plt.title("Query Image")
plt.imshow(queryImg)
plt.show()

# init VGGNet16 model
model = VGGNet()

# extract query image's feature, compute simlarity score and sort
queryVec = model.extract_feat(queryDir)
scores = np.dot(queryVec, feats.T)
rank_ID = np.argsort(scores)[::-1]
rank_score = scores[rank_ID]
# print rank_ID
# print rank_score


# number of top retrieved images to show
maxres = 3
imlist = [imgNames[index] for i, index in enumerate(rank_ID[0:maxres])]
print("top %d images in order are: " % maxres, imlist)

# show top #maxres retrieved result one by one
for i, im in enumerate(imlist):
    image = mpimg.imread(args["result"] + "/" + im.decode("utf-8"))
    plt.title("search output %d" % (i + 1))
    plt.imshow(image)
    plt.show()
