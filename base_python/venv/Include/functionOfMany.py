x = float(input('x='))
if x>1:
    y = x*3-5
elif x>=-1:
    y=x+2
else:
    y=x*5+3
print('f(%.2f)=%.2f' %(x,y))