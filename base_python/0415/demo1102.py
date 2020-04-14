# 查看字典方法 setdefault 的文档，并使用该方法写一个更简洁的 invert_dict
from __future__ import print_function, division


def invert_dict(d):
    """
    反转字典，key变成value，
    :param d:
    :return:
    """
    inverse = {}
    for key in d:
        val = d[key]
        inverse.setdefault(val, []).append(key)
    return inverse


if __name__ == '__main__':
    d = dict(a=1, b=2, c=3, z=1)
    inverse = invert_dict(d)
    print(inverse)
    for val in inverse:
        keys = inverse[val]
        print(val, keys)
