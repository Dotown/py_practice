# python中函数的参数可以有默认值，而且支持可变参数。因此python没有函数重载
from random import randint
def roll(n=2):
    result = 0
    for x in range(n):
        result+=randint(1,6)
    return result

def add(a=0,b=0,c=0):
    return a+b+c

def anyadd(*args):  # 任意数量的参数
    total = 0
    for val in args:    # args的列表为各个val的值
        total+=val
    return total

print(roll())
print(roll(5))
print(add(1,2,3))
print(add(1,2))
print(anyadd(1,2,3,4,5))