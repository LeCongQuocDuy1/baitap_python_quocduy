from abc import abstractmethod


class Shape:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @abstractmethod
    def chuvi(self):
        pass

    @abstractmethod
    def dientich(self):
        pass