# 编写一函数，读取 words.txt 中的单词并存储为字典中的键。值是什么无所谓。
# 然后，你可以使用 in 操作符检查一个字符串是否在字典中。


def read_dict():
    # 生成一个字典
    d = dict()
    # 读取word文件中的单词
    fin = open('words.txt')
    for line in fin:
        word = line.split(' ')
    # 转为list，然后存储kv
    for i in range(len(word)-1):
        d[word[i]] = word[i]
    return d


def is_exist(key):
    d = read_dict()
    return key in d


if __name__ == '__main__':
    print(is_exist('love'))


