flag0 = 1==1    # True
flag1 = 3 > 2   # True
flag2 = 3 < 2   # False
flag3 = flag1 and flag2 # False
flag4 = flag1 or flag2  # True
print('flag0 =', flag0)
print('flag1 =', flag1)
print('flag2 =', flag2)
print('flag3 =', flag3)
print('flag4 =', flag4)
print(flag2 is not False) # 输出False is和is not为身份运算符