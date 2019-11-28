# 实现1~100之间的偶数求和
sum=0
for x in range(101):
    if x%2 == 0:
        sum+=x
print("偶数的总和为：%d" %sum)
print(sum)
# ------------第二种做法
summary=0
for y in range(2,101,2):
    summary+=y
print(summary)