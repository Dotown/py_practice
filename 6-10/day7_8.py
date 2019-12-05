# 生成式与生成器
import sys
f = [x for x in range(1, 10)]
print(f)
f = [x+y for x in 'ABCDE' for y in '123']
print(f)
f = [x**2 for x in range(1, 10)]
print(sys.getsizeof(f))  # 查看对象占用内存的字节数
print(f)

f = (x ** 2 for x in range(1, 10))
print(sys.getsizeof(f))  # 相比生成式生成器不占用存储数据的空间
print(f)
for val in f:
    print(val)