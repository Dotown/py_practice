# 通过yield关键字将一个普通函数改造成生成器函数
# a = 0, b = 1报错
def fib(n):
    a,b = 0,1
    for i in range(n):
        a,b = b,a+b
        yield a

def main():
    for val in fib(20):
        print(val)
# 生成器函数：常规函数定义，但是使用yield语句而不是return 语句返回结果，yield语句一次返回一个结果，可以使用多次，在每
# 个结果中间，挂起函数的状态，以便下次从它离开的地方继续执行。
if __name__ == '__main__':
    main()