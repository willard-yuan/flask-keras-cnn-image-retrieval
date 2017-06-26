# Image Retrieval Engine Based on Keras

## 环境

```python
In [1]: import keras
Using Theano backend.
```

keras 2.0.1 及 2.0.5 版本均经过测试可用。

### 使用

python extract.py -database <path-to-dataset> -index <path-for-extracted-feature>

```sh
├── database 图像数据集
├── extract_cnn_vgg16_keras.py 对图像数据集提取特征
├── query_online.py 库内搜索
└── README.md
```

### 更新

- 针对近期有小伙伴反映的keras版本的问题，已将其进行到最新版本，并且特征提取代码大幅精简。

### Goal
重新用flask写CNN-Web-Demo-for-Image-Retrieval，并使用keras使它支持在线上传功能。
