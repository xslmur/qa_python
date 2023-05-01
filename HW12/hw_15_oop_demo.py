import abc
import math


class Figure(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_area(self):
        """returns figure area"""
        return

    @abc.abstractmethod
    def get_perimeter(self):
        """returns figure perimeter"""
        return


class Triangle(Figure):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_area(self):
        """returns triangle area (Heron's formula)
           https://en.wikipedia.org/wiki/Heron%27s_formula
        """
        s = self.get_perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def get_perimeter(self):
        """returns triangle perimeter"""
        return self.a + self.b + self.c


class Circle(Figure):
    def __init__(self, r):
        self.r = r

    def get_area(self):
        """returns circle area"""
        return math.pi * (self.r ** 2)

    def get_perimeter(self):
        """returns circle perimeter"""
        return 2 * math.pi * self.r


class Rectangle(Figure):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_area(self):
        """returns rectangle area"""
        return self.a * self.b

    def get_perimeter(self):
        """returns rectangle perimeter"""
        return self.a + self.a + self.b + self.b


class Square(Rectangle):
    def __init__(self, a):
        super().__init__(a, a)


def test_figure(figure_class, *args):
    f = figure_class(*args)
    area = f.get_area()
    perimeter = f.get_perimeter()
    print('figure: {}({}) area:{} perimeter:{}'.format(
        type(f).__name__, args, area, perimeter))


test_figure(Triangle, 3, 3, 3)
test_figure(Circle, 20)
test_figure(Rectangle, 5, 6)
test_figure(Square, 5)