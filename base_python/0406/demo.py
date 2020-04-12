# 编写一个函数，读取文件 words.txt ，建立一个列表,其中每个单词为一个元素。
# 编写两个版本，一个使用 append 方法，另一个使用 t = t + [x] 。
# 那个版本运行得慢？为什么？
import time

def make_word_list1():
    """
    读取文件中的单词
    :return:
    """
    t = []
    # 读取文件
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        t.append(word)
    return t


def make_word_list2():
    """
    使用t=t+word
    :return:
    """
    t = []
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        t = t + [word]
    return t


if __name__ == '__main__':
    start_time = time.time()
    t = make_word_list1()
    spend_time = time.time() - start_time

    print(len(t))
    print(t[:10])
    print(spend_time, 'seconds')

    start_time = time.time()
    t = make_word_list2()
    elapsed_time = time.time() - start_time

    print(len(t))
    print(t[:10])
    print(elapsed_time, 'seconds')


