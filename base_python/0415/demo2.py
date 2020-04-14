# 如果你做了习题10-7，你就已经写过一个叫 has_duplicates 的函数，它接受一个列表作为参数，
# 如果其中有某个对象在列表中出现不止一次就返回True。

def has_duplicate(t):
    """
    整体的思路是，搜索不在d中的kv，如果重复则不保存，最后比较长度，如果一样则表示没有重复，
    如果不一样，咋表示有重复
    字典里面是否有重复的,使用for循环
    :param t:
    :return:True 没有重复
    """
    d = {}
    for x in t:
        if x not in d:
            # 根据key值获取v值
            d[x] = t[x]
    return len(d) == len(t)


def has_duplicates(t):
    """

    :param t:
    :return: False 不重复 True重复
    """
    d = {}
    for x in t:
        if x in d:
            return True
        d[x] = True
    return False


def has_duplicates2(t):
    return len(set(t) < len(t))

if __name__ == '__main__':
    t = [1, 2, 3]
    print(has_duplicates(t))
    t.append(1)
    print(has_duplicates(t))
    d = dict(a=1, b=2, c=3, z=1)
    print(has_duplicates(d))
