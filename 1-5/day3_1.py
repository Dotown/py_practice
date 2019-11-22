username = input('请输入用户名：')
password = input('请输入密码：')
if username == 'admin' and password == '123456':
    print('输入正确')
else:
    print('密码错误')
# 如果if条件下要执行多条语句，只需要保持相同的缩进即可。