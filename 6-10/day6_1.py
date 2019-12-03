def factorial(num):
    result = 1
    for n in range(1,num+1):
        result *= n
    return result
m = int(input('m ='))
n = int(input('n ='))
print(factorial(m)//factorial(n)//factorial(m-n))
# 当需要计算阶乘的时候直接使用math中的factorial函数即可
