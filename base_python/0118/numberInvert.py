# 正整数反转，例如：将12345变成54321，
num = int(input("请输入反转的数字"))
reverse_num = 0
while num > 0:
    reverse_num = reverse_num * 10 + num % 10
    num //= 10
print(reverse_num)
