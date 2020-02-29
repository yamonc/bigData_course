# 将1-9999之间的素数分别写入三个文件中（1-99之间的素数保存在a.txt中，
# 100-999之间的素数保存在b.txt中，
# 1000-9999之间的素数保存在c.txt中）
from math import sqrt


def is_prime(n):
    """
    判断是否是素数
    :param n: 输入值
    :return: 是返回true 否则false
    """
    assert n > 0
    for factor in range(2, int(sqrt(n))+1):
        if n % factor == 0:
            return False
    return True if n != 1 else False

def main():
    filenames = ('a.txt', 'b.txt', 'c.txt')
    fs_list = []
    try:
        for filename in filenames:
            fs_list.append(open(filename, 'w',encoding='utf-8'))
        for number in range(1, 10000):
            if is_prime(number):
                fs_list[0].write(str(number) + '\n')
            elif number < 1000:
                fs_list[1].write(str(number) + '\n')
            else:
                fs_list[2].write(str(number) + '\n')
    except IOError as ex:
        print(ex)
        print('写入文件时候发生错误')
    finally:
        for fs in fs_list:
            fs.close()
        print('操作完成!')


if __name__ == '__main__':
    main()
