# 编写一个叫做 nested_sum 的函数，接受一个由一些整数列表构成的列表作为参数，并将所有嵌套列表中的元素相加。 例如：
#
# >>> t = [[1, 2], [3], [4, 5, 6]]
# >>> nested_sum(t)
# 21


def nested_sum(t):
    '''
    t: list of numbers
    :param t:
    :return:
    '''
    total = 0
    for nested in t:
        total += sum(nested)
    return total

# 编写一个叫做 cumsum 的函数，接受一个由数值组成的列表，并返回累加和；
# 即一个新列表，其中第i个元素是原列表中前i+1个元素的和。 例如：
# >>> t = [1, 2, 3]
# >>> cumsum(t)
# [1, 3, 6]


def cumsum(t):
    total = 0
    res = []
    for x in t:
        total += x
        res.append(total)
    return res

# 编写一个叫做 middle 的函数，接受一个列表作为参数，并返回一个除了第一个和最后一个元素的列表。 例如：
# >>> t = [1, 2, 3, 4]
# >>> middle(t)
# [2, 3]


def middle(t):
    '''
    返回除了第一个和最后一个元素的列表
    :param t:
    :return:
    '''
    return t[1:-1]


def chop(t):
    '''
    编写一个叫做 chop 的函数，接受一个列表作为参数，移除第一个和最后一个元素，并返回None。 例如：
     t = [1, 2, 3, 4]
    chop(t)
     t
        [2, 3]
    :param t:
    :return:
    '''
    del t[0]
    del t[-1]


def is_sorted(t):
    '''
    编写一个叫做``is_sorted``的函数，接受一个列表作为参数， 如果列表是递增排列的则返回 True ，否则返回False。 例如：
    is_sorted([1, 2, 2])
    True
    is_sorted(['b', 'a'])
    False
    :param t:
    :return:
    '''
    return t == sorted(t)



if __name__ == '__main__':
    # t = [[1, 2], [3], [4, 5, 6]]
    # print('总和为', nested_sum(t))

    t = [1, 2, 3, 5]
    print(is_sorted(t))
