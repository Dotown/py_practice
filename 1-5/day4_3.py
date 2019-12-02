import random
answer = random.randint(1, 100)
counter = 0
while True:
    number = int(input('请输入：'))
    counter += 1    # python不能使用counter++
    if number > answer:
        print('大了')
    elif number < answer:
        print('小了')
    else:
        print('回答正确')
        break   # break可以提前结束循环，但是只能结束当前循环。
                # continue可以放弃本次循环，直接进入下一次循环。
print('总共回答了%d次' % counter)