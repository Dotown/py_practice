a = float(input('请输入a的长度'))
b = float(input('请输入b的长度'))
c = float(input('请输入c的长度'))
if a+b>c and b+c>a and a+c>b:
    print('周长为%.1f' % (a+b+c))
    p = (a+b+c)/2
    s = (p*(p-a)*(p-b)*(p-c))**0.5
    print('面积为%.1f' % s)
else:
    print('无法构成三角形')
# a**b 意思是a的b次方
# pow(a,b) 也一样