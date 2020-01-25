# 实现计算求最大公约数和最小公倍数的函数。
def gcd(x, y):
    """" 求最大公约数 """
    if x > y:
        (x, y) = (y, x)
    else:
        (x, y) = (x, y)
    for factor in range(x, 0, -1):
        if x % factor == 0 and y % factor == 0:
            return factor


def lcm(x, y):
    return x * y // gcd(x, y)


if __name__ == '__main__':
    print('最大公约数：')
    g = gcd(12, 16)
    print(g)
    print('最小公倍数：')
    l = lcm(12, 16)
    print(l)
