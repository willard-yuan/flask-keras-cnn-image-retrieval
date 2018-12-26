# Image Retrieval Engine Based on Keras

[![License](https://img.shields.io/badge/license-BSD-blue.svg)](../LICENSE)

## 演示

[演示地址](http://202.120.39.161:55555/)(不能访问，没钱续VPS了)，跑在CPU上，web界面采用的[SoTu](https://github.com/willard-yuan/SoTu)

## 环境

```python
In [1]: import keras
Using Theano backend.
```

keras 2.0.1 及 2.0.5 版本均经过测试可用。推荐Python 2.7，支持Python 3.6.

此外需要numpy, matplotlib, os, h5py, argparse. 推荐使用anaconda安装

### 使用

- 步骤一

`python index.py -database <path-to-dataset> -index <name-for-output-index>`

- 步骤二

`python query_online.py -query <path-to-query-image> -index <path-to-index-flie> -result <path-to-images-for-retrieval>`

```sh
├── database 图像数据集
├── extract_cnn_vgg16_keras.py 使用预训练vgg16模型提取图像特征
|── index.py 对图像集提取特征，建立索引
├── query_online.py 库内搜索
└── README.md
```

#### 示例

```sh
# 对database文件夹内图片进行特征提取，建立索引文件featureCNN.h5
python index.py -database database -index featureCNN.h5

# 使用database文件夹内001_accordion_image_0001.jpg作为测试图片，在database内以featureCNN.h5进行近似图片查找，并显示最近似的3张图片
python query_online.py -query database/001_accordion_image_0001.jpg -index featureCNN.h5 -result database
```


### 更新

- 针对近期有小伙伴反映的keras版本的问题，已将其进行到最新版本，并且特征提取代码大幅精简。
- 显示检索得到的图片， 可自由定义查询图片及检索图片集

### Goal

- [x] 重新用flask写web界面，已完成。

### 论文推荐

[**awesome-cbir-papers**](https://github.com/willard-yuan/awesome-cbir-papers)

### 问题汇总

- `query_online.py` line 28报错，将`index.py` line 62注释，使用line 61.
