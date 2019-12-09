# 集合
set1 = {1, 2, 3, 3, 4}
print('set1=', set1) # {1, 2, 3, 4}
# 创建集合的构造器语法
set2 = set(range(1, 10))
set3 = set((1, 2, 3, 3, 2, 1))
print(set2, set3)

set4 = {num for num in range(1, 20) if num%3 == 0 or num%5 == 0}    # num for num
print('set4=', set4)

# 添加元素以及删除元素
set1.add(5) #添加单个元素
set1.update([10, 11])    # 添加多个元素
set2.discard(9)
print(set1, set2)

# 集合的交集、并集、差集、对称差运算
print('集合的交集、并集、差集、对称差运算:')
print(set1 & set2)
# print(set1.intersection(set2))
print(set1 | set2)
# print(set1.union(set2))
print(set1 - set2)
# print(set1.difference(set2))
print(set1 ^ set2)  # 元素只存在其中一个集合中
# print(set1.symmetric_difference(set2))
# 判断子集和超集
print(set2 <= set1)
# print(set2.issubset(set1))
print(set3 <= set1)
# print(set3.issubset(set1))
print(set1 >= set2)
# print(set1.issuperset(set2))
print(set1 >= set3)
# print(set1.issuperset(set3))
