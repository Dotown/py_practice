from random import randint
money =1000
while money>0:
    x = int(input('请下注'))
    first = randint(1,6)+randint(1,6)
    if first ==7 or first ==11:
        money = money +x
        print('第一次点数为%d，你赢了，还有%d元' % (first,money))
    elif first == 2 or first ==3 or first ==12:
        money = money -x
        print('第一次点数为%d，你输了，还有%d元' % (first, money))
    else:
        while True:
            num = randint(1,6)+randint(1,6)
            if num ==7:
                money = money-x
                print('第一次点数为%d，这次点数为%d，你输了，还有%d元' % (first, num, money))
                break
            elif num ==first:
                money = money+x
                print('第一次点数为%d，这次点数为%d，你赢了，还有%d元' % (first, num, money))
                break
