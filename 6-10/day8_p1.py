import time


class Click(object):
    def __init__(self, hour = 0, minute = 0, second = 0):
        self.__hour = hour
        self.__minute = minute
        self.__second = second
    def run(self):
        self.__second += 1
        if(self.__second >= 60):
            self.__second = 0
            self.__minute += 1
            if(self.__minute >= 60):
                self.__minute = 0
                self.__hour += 1
                if(self.__hour == 24):
                    self.__hour = 0
    def show(self):
        print('现在时间为%02d:%02d:%02d'%(self.__hour,self.__minute,self.__second))

def main():
    click = Click(23,59,58) # click = Click()
    while(True):
        click.show()
        time.sleep(1)
        click.run()


if __name__ == '__main__':
    main()