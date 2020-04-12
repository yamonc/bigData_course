# 假设给你一个字符串，你想计算每个字母出现的次数
def count_num(s):
    d = dict()
    for a in s:
        if a not in d:
            d[a] = 1
        else:
            d[a] +=1
    return d


def print_hist(h):
    for c in h:
        print(c, h[c])


if __name__ == '__main__':
    s = 'abcabcdda'
    d = count_num(s)
    print_hist(d)
    for key in sorted(d):
        print(key, d[key])

    print(d)

