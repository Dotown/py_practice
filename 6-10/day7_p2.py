import random
def creat_code(num = 4):
    str = '0123456789abcdefghijklmnokqrstuvwxyzABCDEFGHIIJKLMNOPQRSTUVWXYZ'
    code = ''
    for i in range(num):
        code += str[random.randint(0, len(str)-1)]
    return code
if __name__  =='__main__':
    print(creat_code(5))

