s1 = 'hello '*3
s2 = 'world'
s1 += s2
print(s1)
print('lo' in s1)
print('ld' not in s2)
str = 'abc123456'
print(str[2])   # str的第三个字符
print(str[2:5]) # c12 str的第三个到第六个字符 包括三，不包括六
print(str[2:]) # c123456 str的第三个字符到最后一个字符
print(str[2::2]) # c246 str的第三个字符开始，隔一个字符取一个
print(str[::2]) # ac246
print(str[::-1]) # 654321cba str开头开始，倒着取
print(str[-3:-1]) # 45