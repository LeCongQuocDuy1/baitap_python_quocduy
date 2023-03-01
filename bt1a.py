def check_odd_even_bit(n):
    # flag = 1 => số lẻ
    # flag = 0 => số chẵn

    flag = 0;
    if (n & 1 == 1):
        flag = 1
    return flag


n = int(input(">> nhap mot so: "))

check = check_odd_even_bit(n);

if check == 1:
    print(n, "la so le")
else:
    print(n, "la so chan")