import os
import numpy as np
import matplotlib.pyplot as plt
import pylab
# 特征提取
from skimage import io, filters, color
# 利用邻近点方式训练数据
from sklearn.neighbors import KNeighborsClassifier
# 将数据分为测试集和训练集
from sklearn.model_selection import train_test_split


# 获取路径
def all_path(dirname):
    result = []  # 所有的文件
    for maindir, subdir, file_name_list in os.walk(dirname):
        for filename in file_name_list:
            # 合并成一个完整路径
            apath = os.path.join(maindir, filename)
            result.append(apath)
    return result


# 用来正常显示中文标签
plt.rcParams['font.sans-serif'] = ['SimHei']

# 引入数据集和标签
# D:\\DataSet\\缺陷图像集
path = "G:\\研究生文件\\研一\\机器学习\\缺陷图像集"
data = []
labels = []
# 循环输入的图片 获取标签
paths = all_path(path)
for imagePath in paths:
    image = io.imread(imagePath)
    data.append(image)

    # 边缘检测
    # edge = filters.sobel(image)
    # edge_gray = color.rgb2grey(edge)
    # data.append(edge)
    # plt.imshow(edge, plt.cm.gray)

    # 阈值分割
    # thresh = filters.threshold_otsu(image)  # 返回一个阈值
    # dst = image <= thresh  # 根据阈值进行分割
    # data.append(dst)

    # plt.imshow(dst, plt.cm.gray)
    # plt.show()
    # 获取文件的标签
    label = imagePath.split(os.path.sep)[-2]
    # 获取标签集
    labels.append(label)
# 提取训练集
# 利用train_test_split进行将训练集和测试集进行分开，test_size占20%
X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2)

# 引入训练方法
knn = KNeighborsClassifier(n_neighbors=5)

X_train = np.asarray(X_train)
y_train = np.asarray(y_train)
X_test = np.asarray(X_test)
y_test = np.asarray(y_test)
nsamples, nx, ny = X_train.shape
X_train = X_train.reshape(nsamples, nx * ny)
nsamples2, nx2, ny2 = X_test.shape
i = 0
for X in X_test:
    plt.title(i)
    plt.imshow(X, plt.cm.gray)
    # plt.show()
    i = i + 1
X_test = X_test.reshape(nsamples2, nx2 * ny2)
knn.fit(X_train, y_train)
y = knn.predict(X_test)

print(y)
print("直接比真实值和预测值：\n", y_test == y)

score = knn.score(X_test, y_test)
print("准确率为：\n", score)
