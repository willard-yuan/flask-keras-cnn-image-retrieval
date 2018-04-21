# -*- coding:utf-8 -*-
import subprocess


def create_index():
    process = subprocess.Popen(["python", "index.py", "-database", "database", "-index", "featureCNN.h5"])
    process.wait()


def search():
    process = subprocess.Popen(
        ["python", "query_online.py", "-query", "database/001_accordion_image_0001.jpg",
         "-index", "featureCNN.h5", "-result", "database"]
    )
    process.wait()


if __name__ == '__main__':
    # create_index()

    search()
