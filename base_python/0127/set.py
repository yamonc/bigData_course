# 使用集合
# 创建集合的字面量语言
set1 = {1, 2, 3, 3, 3, 2}
print(set1)
print('Length:', len(set1))
# 创建集合的构造器语法
set2 = set(range(1, 10))
set3 = set((1, 2, 3, 3, 2, 1))
print(set2, set3)
# 创建集合的推导式语法(推导式也可以用于推导集合)
set4 = {num for num in range(1, 100) if num % 3 == 0 or num % 5 == 0}
print('set4:', set4)
set5 = {1}
for num in range(1, 100):
    if num % 3 == 0 or num % 5 == 0:
        set5.add(num)
set5.remove(1)
print('set5', set5)
# 添加元素 删除元素
set1.add(4)
print(set1)
set2.update([11, 12])
print(set2)
set2.discard(5)
print(set2)
if 4 in set2:
    set2.remove(4)
print(set2)
# 集合的成员、交集、并集、差集等运算
print('操作前的集合：')
print('set1:', set1)
print('set2:', set2)
# 交集：
print(set1 & set2)
print(set1.intersection(set2))
# 并集
print(set1 | set2)
# print(set1.union(set2))
# 差集
print(set1 - set2)
# print(set1.difference(set2))
# 判断子集和超集
print(set2 <= set1)
# print(set2.issubset(set1))
print(set3 <= set1)
# print(set3.issubset(set1))
print(set1 >= set2)
# print(set1.issuperset(set2))
print(set1 >= set3)
# print(set1.issuperset(set3))

