# 计算机出一个1~100之间的随机数，人输入自己猜的数字，计算机给出对应的提示信息，直到人猜出计算机出的数字
# 产生一个随机数
import random
answer = random.randint(1,100)
counter = 0
while True:
    counter+=1
    mumber = int(input('请输入'))
    if mumber < answer:
        print('大一点')
    elif mumber > answer:
        print('小一点')
    else:
        print('恭喜你，猜对了')
        break
print('你一共猜了%d次' % counter)
if counter >7:
    print('智商有限')