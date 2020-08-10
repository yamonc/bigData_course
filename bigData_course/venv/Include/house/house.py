import paddle.fluid as fluid
import paddle
import numpy as np
import os
import matplotlib.pyplot as plt


BUF_SIZE = 500
BATCH_SIZE = 20

# 用于训练的数据提供器，每次从缓存中随机读取批次大小的数据
train_reader = paddle.