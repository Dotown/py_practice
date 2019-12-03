s1 = '\'hello,world\''
s2 = '\n\\hello\\\n'
print(s1, s2)    # 这种方式的s1和s2为连续输出

# 加r之后的\不进行转义
s3 = r'\'hello,world\''
s4 = r'\n\\hello\\\n'
print(s3, s4)

s5 = '\141\142\143\x61\x62\x63'
s6 = '\u9a86\u660a'
print(s5, s6)