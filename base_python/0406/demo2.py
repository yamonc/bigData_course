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


def reverse_lookup(d, v):
    for k in d:
        if d[k] == v:
            return k
    raise LookupError()


# 在字典中，列表可以作为值出现。
# 例如，如果你有一个从字母映射到频率的字典， 而你想倒转它； 也就是生成一个从频率映射到字母的字典。
# 因为可能有些字母具有相同的频率，所以在倒转字典中的每个值应该是一个字母组成的列表。
# 倒转字典
def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse


if __name__ == '__main__':
    s = 'abcabcdda'
    d = count_num(s)
    print_hist(d)
    for key in sorted(d):
        print(key, d[key])

    print(d)
    print(reverse_lookup(d, 3))
    print(invert_dict(d))


