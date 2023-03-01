import math


# Bài 4: Tính sqrt(1+x)
def myBuild1(x):
  mu = 2
  operator = 0
  k = 0.00000000000000000001
  tu = 1
  hstu = 3
  mau = 2 * 4
  hsmau = 6
  f = 1
  s = f + 1 / 2 * x

  while (abs(f - s) > k):
    f = s
    if operator == 0:
      s = f - (tu / mau * x**mu)
      operator = 1
    else:
      s = f + ((tu / mau) * x**mu)
      operator = 0

    mu = mu + 1
    tu = tu * hstu
    mau = mau * hsmau
    hstu = hstu + 2
    hsmau = hsmau + 2

  print("Tự  tính: ", f)


def fac1(x):
  print("Máy tính: ", math.sqrt(1 + x))


# Bài 5: Tính 1/sqrt(1+x)
def myBuild2(x):
  mu = 2
  operator = 1
  k = 0.00000000000000000001
  tu = 3
  hstu = 5
  mau = 2 * 4
  hsmau = 6
  f = 1
  s = f - 1 / 2 * x

  while (abs(f - s) > k):
    f = s
    if operator == 0:
      s = f - (tu / mau * x**mu)
      operator = 1
    else:
      s = f + ((tu / mau) * x**mu)
      operator = 0

    mu = mu + 1
    tu = tu * hstu
    mau = mau * hsmau
    hstu = hstu + 2
    hsmau = hsmau + 2

  print("Tự  tính: ", f)


def fac2(x):
  print("Máy tính: ", 1 / math.sqrt(1 + x))


#
#
# Bài 2: Tính 1/sqrt(1+x)
def myBuild3(x):
  mu = 2
  operator = 1
  k = 0.0000000000000000001
  f = 1
  s = f - (2 * 3 / 2) * x
  while (abs(f - s) > k):
    f = s
    if operator == 0:
      s = f - (((mu + 1) * (mu + 2)) / 2) * x**mu
      operator = 1
    else:
      s = f + (((mu + 1) * (mu + 2)) / 2) * x**mu
      operator = 0

    mu = mu + 1

  print("Tự  tính: ", f)


def fac3(x):
  s = 1 / ((1 + x)**3)
  print("Máy tính: ", s)


print("Bài 4: Tính sqrt(1+x)")
myBuild1(0.6)
fac1(0.6)

print("")
print("Bài 5: Tính 1/sqrt(1+x)")
myBuild2(0.6)
fac2(0.6)

print("")
print("Bài 2: Tính 1/(1+x)**3")
myBuild3(0.6)
fac3(0.6)
