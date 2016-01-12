import numpy as np
import h5py

h5f = h5py.File('featsCNN.h5','r')
feats = h5f['dataset_1'][:]
imgNames = h5f['dataset_2'][:]
h5f.close()

queryVec = feats[0]
scores = np.dot(queryVec, feats.T)

rank_ID = np.argsort(scores)[::-1]
rank_score = scores[rank_ID]
#print rank_ID
print rank_score

maxres = 6
imlist = [imgNames[index] for i,index in enumerate(rank_ID[0:maxres])]
print imlist
