class Test(object):
    def __init__(self, one, two):
        self.__one = one
        self.two = two
    def __pr(self):
        print('one是%s，two是%s'%(self.__one, self.two))
    def pu(self):
        print('one是%s，two是%s'%(self.__one, self.two))

def main():
    test1 = Test('private', 'public')
    # AttributeError: 'Test' object has no attribute '__pr'
    # print(test1.__pr())
    print(test1.pu())
    # AttributeError: 'Test' object has no attribute 'one'
    # print(test1.one)
    print(test1.two)

if __name__ == '__main__':
    main()