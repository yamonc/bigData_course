# 静态方法

from math import sqrt


class Triangle(object):
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    @staticmethod
    def is_valid(a, b, c):
        return a + b > c and b + c > a and a + c > b

    def perimeter(self):
        return self._a + self._b + self._c

    def area(self):
        half = self.perimeter() / 2
        return sqrt(half * (half - self._a) * (half - self._b) * (half - self._c))


def main():
    a, b, c = 3, 4, 5
    # 静态方法和类方法都是通过类发送消息调用
    if Triangle.is_valid(a, b, c):
        # 如果三角形合法
        t = Triangle(a, b, c)
        print(t.perimeter())
        # 也可以通过给类发送消息来调用对象方法，但是要传入接收消息的对象作为参数
        print(t.area())
    else:
        print("无法构成三角形")


if __name__ == '__main__':
    main()