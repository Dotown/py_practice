class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # 在Python中，属性和方法的访问权限只有两种，也就是公开的和私有的，如果希望属性是私有的，在给属性命名时可以用两个下划线作为开头

    def study(self, course_name):
        print('%s正在学习%s'%(self.name, course_name))  #这里的course_name不能加self


    def watch_movie(self):
        if self.age < 18 :
            print('欢迎收看幼儿节目')
        else:
            print('欢迎收看成人节目')

def main():
    stu1 = Student('艾伦', 22)
    stu1.study('python')
    stu1.watch_movie()
    stu2 = Student('小明', 15)
    stu2.study('VB程序设计')
    stu2.watch_movie()


if __name__ == '__main__':
    main()