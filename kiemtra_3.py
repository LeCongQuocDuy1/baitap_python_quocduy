from baitap2 import Shape


class Circle(Shape):

    def __init__(self, x, y, bankinh):
        super().__init__(self, x, y)
        self.bankinh = bankinh

    def chuvi(self):
        return self.bankinh*3.14

    def dientich(self):
        return (2*self.bankinh*3.14) / 4

class Rect(Shape):

    def __init__(self, x, y, chieudai, chieurong):
        super().__init__(self, x, y)
        self.chieudai = chieudai
        self.chieurong = chieurong

    def chuvi(self):
        return (self.chieudai+self.chieurong) * 2

    def dientich(self):
        return self.chieudai*  self.chieurong

import math

class Triangle(Shape):

    def __init__(self, x, y, canh1, canh2, canh3):
        super().__init__(self, x, y)
        self.canh1 = canh1
        self.canh2 = canh2
        self.canh3 = canh3

    def chuvi(self):
        return self.canh1 + self.canh2 + self.canh3

    def dientich(self):
        return math.sqrt((self.chuvi() / 2)*((self.chuvi()/2)-self.canh1)*((self.chuvi()/2)-self.canh2)*((self.chuvi()/2)-self.canh3))