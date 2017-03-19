# -*- coding: utf-8 -*-
# Author: yongyuan.name

from keras.applications.vgg16 import VGG16
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input

import os
import h5py
import numpy as np
from numpy import linalg as LA


def get_imlist(path):
    """    Returns a list of filenames for
        all jpg images in a directory. """
    return [os.path.join(path,f) for f in os.listdir(path) if f.endswith('.jpg')]


if __name__ == "__main__":

    input_shape = (224, 224, 3)

    # weights: 'imagenet'
    # pooling: 'max' or 'avg'
    # input_shape: (width, height, 3), width and height should >= 48
    model = VGG16(weights = 'imagenet', input_shape = (input_shape[0], input_shape[1], 3), pooling = 'max', include_top = False)

    db = "database"
    img_list = get_imlist(db)
    
    feats = []
    names = []

    for i, img_path in enumerate(img_list):
        img = image.load_img(img_path, target_size=(input_shape[0], input_shape[1]))
        img = image.img_to_array(img)
        img = np.expand_dims(img, axis=0)
        img = preprocess_input(img)
        feat = model.predict(img)
        img_name = os.path.split(img_path)[1]
        norm_feat = feat[0]/LA.norm(feat[0])
        feats.append(norm_feat)
        names.append(img_name)
        print "image %d feature extraction, total %d images" %((i+1), len(img_list))

    feats = np.array(feats)
    h5f = h5py.File('featsCNN.h5', 'w')
    h5f.create_dataset('dataset_1', data = feats)
    h5f.create_dataset('dataset_2', data = names)
    h5f.close()
