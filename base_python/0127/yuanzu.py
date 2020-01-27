# 元组：元组与列表类似也是一种容器数据类型，可以用一个变量（对象）来存储多个数据，
# 不同之处在于元组的元素不能修改，在前面的代码中我们已经不止一次使用过元组了。顾名思义，
# 我们把多个元素组合到一起就形成了一个元组，所以它和列表一样可以保存多条数据。
t = ('yamon', 24, True, '河北邯郸')
print(t)
# 获取元组内的内容
print(t[0])
for i in t:
    print(i)
# 重新赋值
t = ('陈亚萌' ,24 ,True , '天津')
print(t)
# 将元组转化为列表：
person = list(t)
print(person)
# 利用列表修改元素，元组不允许修改元素
person[0] = 'yyh'
person[1] = 22
print(person)
# 列表转为元组
fruits_list = ['apple', 'banana', 'orange']
tuple=tuple(fruits_list)
print(tuple)
