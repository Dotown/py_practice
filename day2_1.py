a = int(input('a = '))  # input括号里边是显示的内容
b = int(input('b = '))
print('%d + %d = %d' % (a, b, a + b))   # %d和括号内的变量一一对应
print('%d - %d = %d' % (a, b, a - b))
print('%d * %d = %d' % (a, b, a * b))
print('%d / %d = %f' % (a, b, a / b))   # 除法
print('%d // %d = %d' % (a, b, a // b)) # 取整
print('%d %% %d = %d' % (a, b, a % b))  # %%输出为%
print('%d ** %d = %d' % (a, b, a ** b))