num = int(input('请输入一个整数'))
end = int(num **0.5)
re = True
for i in range(2,end+1):
    if num % i ==0:
        re = False
        break
if re and num!=1:
    print('%d是一个素数'%num)
else:
    print('%d不是一个素数'%num)