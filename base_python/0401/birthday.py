# 如果你的班级上有23个学生， 2个学生生日相同的概率是多少？
# 你可以通过随机产生23个生日，并检查匹配来估算概率。
# 提示：你可以使用 random 模块中的 randint 函 数来生成随机生日。
from __future__ import print_function, division
import random


def has_duplicates(t):
    # 拷贝一份
    s = t[:]
    s.sort()

    # 检查是否相等
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            return True
    return False


def random_bdays(n):
    """
    返回一个1-365天中的任一一天
    :param n:
    :return:
    """
    # 创建列表
    t = []
    for i in range(n):
        bday = random.randint(1, 365)
        t.append(bday)
    return t


def count_matches(num_students, num_simulations):
    """
    产生一个生日和重复的样例
    :param num_students:
    :param num_simulations: 模拟的人数
    :return: int
    """
    count = 0
    for i in range(num_simulations):
        t = random_bdays(num_students)
        if has_duplicates(t):
            count += 1
    return count


def main():
    """
    init
    :return:
    """
    num_students = 23
    num_simulations = 1000
    count = count_matches(num_students, num_simulations)

    print('After %d simulations' % num_simulations)
    print('With %d students ' % num_students)
    print('there were %d simulations with at least one match' % count)


if __name__ == '__main__':
    main()
