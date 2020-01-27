list1 = [1, 3, 5, 7, 100]
print(list1)  # [1, 3, 5, 7, 100]
# 乘号表示列表元素的重复
list2 = ['hello'] * 3
print(list2)  # ['hello', 'hello', 'hello']
# 计算列表长度(元素个数)
print(len(list1))  # 5
# 下标(索引)运算
print(list1[0])  # 1
print(list1[4])  # 100
# print(list1[5])  # IndexError: list index out of range
print(list1[-1])  # 100
print(list1[-3])  # 5
list1[2] = 300
print(list1)  # [1, 3, 300, 7, 100]
# 通过循环用下标遍历列表元素
for index in range(len(list1)):
    print(list1[index])
# 通过for循环遍历列表元素
for elem in list1:
    print(elem)
# 通过enumerate函数处理列表之后再遍历可以同时获得元素索引和值
for index, elem in enumerate(list1):
    print(index, elem)

print('-----------------------------')
# 如何向列表中添加元素以及如何从列表中移除元素
list3 = [1, 3, 5, 7, 100, 200]
# 添加元素
print(list3)
list3.insert(1, 400)
print(list3)
# 合并两个列表
list3 += [1000, 2000]
print(list3)
# 先通过成员运算判断元素是否在列表中，如果存在则删除元素
if 3 in list3:
    list3.remove(3)
if 1234 in list3:
    list3.remove(1234)
print(list3)
# 从指定位置删除元素
list3.pop(0)
list3.pop(len(list3)-1)
print(list3)
