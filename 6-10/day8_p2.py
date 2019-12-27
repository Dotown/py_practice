class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def move(self, x, y):
        self.x +=x
        self.y +=y
    def show(self):
        print("坐标为(%d,%d)"%(self.x, self.y))
    def distance(self, other):  # 比较两个对象中的元素
        xx = self.x - other.x
        yy = self.y - other.y
        s = (xx**2 +yy**2)**0.5
        print("距离为%d"%s)

def main():
    point1 = Point()
    point2 = Point(5,7)
    point1.move(2,3)
    point1.show()
    point2.show()
    point1.distance(point2)

if __name__ == '__main__':
    main()