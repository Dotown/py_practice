num = int(input('请输入行数'))
for i in range(1,num+1):
    while(True):
        if i == 0:
            print()
            break
        else:
            print('*',end = '')
            i-=1

for i in range(1,num+1):
    a = 0
    while(True):
        if a == num:
            print()
            break
        elif a<num-i:
            print(' ',end='')
            a+=1
        else:
            print('*',end='')
            a+=1

for i in range(1,num+1):
    b = 0
    while(True):
        if b == num+i-1:
            print()
            break
        elif b<num-i:
            print(' ',end='')
            b+=1
        else:
            print('*',end='')
            b+=1
""""
Version: 0.1
Author: 骆昊

row = int(input('请输入行数: '))
for i in range(row):
    for _ in range(i + 1):
        print('*', end='')
    print()


for i in range(row):
    for j in range(row):
        if j < row - i - 1:
            print(' ', end='')
        else:
            print('*', end='')
    print()

for i in range(row):
    for _ in range(row - i - 1):
        print(' ', end='')
    for _ in range(2 * i + 1):
        print('*', end='')
    print()
"""