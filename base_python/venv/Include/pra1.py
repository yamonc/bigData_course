#  *
# **
# ***
# ****
# *****
row = int(input('请输入行数：'))
for i in range(row):
   for j in range(i+1):
        print('*',end='')
   print()

#    *
#   **
#  ***
# ****
#*****

for i in range(row):
    for j in range(row):
        if j < row - i - 1:
            print(' ', end='')
        else:
            print('*', end='')
    print()