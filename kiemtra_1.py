from random import random


def generateRec(f):
    a = random.randint(0, 20)
    b = random.randint(0, 20)
    if a > b:
        c = a
        a = b
        b = c
    x = random.randint(-100, 100)
    y = random.randint(-100, 100)
    f.write("#Rect\n")
    f.write("{} {}\n".format(a, b))
    f.write("{} {}\n".format(x, y))


def generateCir(f):
    bk = random.randint(0, 10)
    x = random.randint(-100, 100)
    y = random.randint(-100, 100)
    f.write("#Circle\n")
    f.write("{}\n".format(bk))
    f.write("{} {}\n".format(x, y))


def generateTri(f):
    a, b, c = 0, 0, 0
    while a + b <= c or a + c <= b or \
            b + c <= a:
        a = random.randint(0, 20)
        b = random.randint(0, 20)
        c = random.randint(0, a + b)
    x = random.randint(-100, 100)
    y = random.randint(-100, 100)
    f.write("#Triangle\n")
    f.write("{} {} {}\n".format(a, b, c))
    f.write("{} {}\n".format(x, y))


def createfile(filename="input.txt", amount=1000):
    with open(filename, "w") as f:
        for i in range(amount):
            generateRec(f)
            generateCir(f)
            generateTri(f)
