class Shape:
    shape_number = 0
    __area = 0
    def __init__(self):
        Shape.shape_number +=1
    def _calc_area(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
        super().__init__()
    def calc_area(self):
        print('圆的面积是：')
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self,length,width):
        super().__init__()
        self.length = length
        self.width = width
    def calc_area(self):
        print('矩形的面积是：')
        return self.length * self.width

c1 = Circle(5)
c2 = Circle(12)
r1 = Rectangle(4,5)
r2 = Rectangle(6,7)

print(c1.calc_area())
print(c2.calc_area())
print(r1.calc_area())
print(r2.calc_area())
print(f"共创建了{c1.shape_number}个图形对象")
