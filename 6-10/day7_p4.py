def max2(str):
    if str[0] > str[1]:
        x, y = str[0], str[1]
    else:
        x, y = str[1], str[0]
    for num in range(2, len(str)):
        if str[num] > x:
            x, y = str[num], x
        elif str[num] < x and str[num] > y:
            y = str[num]
    return x, y

if __name__ == '__main__':
    str  = input('请输入一串数字：')
    print(str)
    print(max2(str))