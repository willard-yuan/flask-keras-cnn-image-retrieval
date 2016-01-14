# image retrieval engine based on Keras

Goal:
重新用flask写CNN-Web-Demo-for-Image-Retrieval，并使用keras使它支持在线上传功能。

[Model visualization](http://keras.io/visualization/)

```sh
➜  flask-keras-cnn-image-retrieval git:(master) ✗ python deep_dream.py ~/Pictures/Lenna.png results/dream
Using Theano backend.
Traceback (most recent call last):
  File "deep_dream.py", line 83, in <module>
    model.add(Convolution2D(64, 3, 3, activation='relu', name='conv1_1'))
  File "/Users/willard/anaconda/lib/python2.7/site-packages/keras/layers/convolutional.py", line 254, in __init__
    super(Convolution2D, self).__init__(**kwargs)
  File "/Users/willard/anaconda/lib/python2.7/site-packages/keras/layers/core.py", line 41, in __init__
    assert kwarg in allowed_kwargs, 'Keyword argument not understood: ' + kwarg
AssertionError: Keyword argument not understood: name
```
