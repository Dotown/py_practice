x = float(input('请输入x的值'))
if x>1:
    y = 3*x-1
elif x >= -1 and x >= 1:    # else if 在python中简写为elif
    y = x+2
else:
    y = 5*x+3
print('y的值为%d' % y)