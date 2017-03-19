# Image Retrieval Engine Based on Keras

## 环境

```python
In [1]: import keras
Using Theano backend.

In [2]: print keras.__version__
2.0.1
```

keras为最新的2.0.1版本

### 使用

```sh
├── database 图像数据集
├── extract_cnn_vgg16_keras.py 对图像数据集提取特征
├── query_online.py 库内搜索
└── README.md
```

### Goal
重新用flask写CNN-Web-Demo-for-Image-Retrieval，并使用keras使它支持在线上传功能。
