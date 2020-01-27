# 列表解析：根据已有列表，高效创建新列表的方式。
# 　　列表解析是Python迭代机制的一种应用，它常用于实现创建新的列表，因此用在[]中。
# 语法：
# 　　[expression for iter_val in iterable]
# 　　[expression for iter_val in iterable if cond_expr]

# 1. 要求：列出1-10所有的数字之和的平方
# 1. 直接的方法：
l = []
for i in range(1, 11):
    l.append(i ** 2)
print(l)
# 2. 使用列表解析
l = [i ** 2 for i in range(1, 11)]
print(l)

# 2.  要求：列出1~10中大于等于4的数字的平方
# 2.1.1：使用普通方法：
for i in range(1, 11):
    if i > 4:
        print(i ** 2)
# 2.1.2 ： 使用列表：
l = []
for i in range(1, 11):
    if i > 4:
        l.append(i ** 2)
print(l)
# 使用列表解析：
# 　　[expression for iter_val in iterable if cond_expr]
l = [i ** 2 for i in range(1, 11) if i > 4]
print(l)

# 补充：
f = [x + y for x in 'ABCDE' for y in '1234567']
print(f)
test = []
for x in 'ABCDE':
    for y in '1234567':
        test.append(x+y)
print(test)

