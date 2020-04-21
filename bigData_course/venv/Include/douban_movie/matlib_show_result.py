import matplotlib.pyplot as plt
import matplotlib
import pandas as pd

if __name__ == '__main__':
    df = pd.read_excel('豆瓣电影250.xls')

    # 配置中文字体和修改字体大小
    matplotlib.rcParams['font.family'] = 'SimHei'
    matplotlib.rcParams['font.size'] = 20
    plt.figure(figsize=(20, 5))
    plt.subplot(1, 2, 1)
    plt.scatter(df['评分'], range(1, 251))
    plt.xlabel('评分')
    plt.ylabel('排名')
    # 修改y轴为倒序
    plt.gca().invert_yaxis()
    # 集中趋势的直方图
    plt.subplot(1, 2, 2)
    plt.hist(df['评分'], bins=15)