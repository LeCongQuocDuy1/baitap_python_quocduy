def readFileText(url):
    with open(url, "r") as file:
        # tách dữ liệu trong file thành các phần tử tách nhau bởi khoảng trắng
        data = file.read().split()
        # chuyển các phần tử trong mảng thành số nguyên
        numbers = [int(x) for x in data]
        return numbers
# kiểm tra số lượng số chẵn và số lượng số lẻ


def soChanLe(listNumber):
    soChan = 0
    soLe = 0
    for i in range(len(listNumber)):
        if listNumber[i] % 2 == 0:
            soChan += 1
        else:
            soLe += 1
    print("Tong so chan: ", soChan)
    print("Tong so le: ", soLe)
# kiểm tra số lượng số nguyên tố


def soNguyenTo(listNumber):
    soNguyenTo = 0
    for i in range(len(listNumber)):
        if listNumber[i] > 1:
            for j in range(2, listNumber[i]):  # kiểm tra từ số 2 đến số đó
                if listNumber[i] % j == 0:
                    break
            else:
                soNguyenTo += 1
    print("So luong so nguyen to: ", soNguyenTo)

# kiểm tra số nào xuất hiện nhiều nhất trong mạng


def soXuatHienNhieuNhat(listNumber):
    soXuatHienNhieuNhat = 0
    soLanXuatHien = 0
    # lấy lần lượt từng số trong mảng so sánh với các số còn lại
    for i in range(len(listNumber)):
        count = 0
        for j in range(len(listNumber)):
            if listNumber[i] == listNumber[j]:
                count += 1  # đếm số lần xuất hiện của số đó = count
                # gán số vừa rồi vào số xuất hiện nhiều nhất

                # nếu count( số hiện tại) > số count (số trước đó thì mình gán số hiện tại vào số xuất hiện nhiều nhất)
        if count > soLanXuatHien:
            soLanXuatHien = count
            soXuatHienNhieuNhat = listNumber[i]
    print("So xuat hien nhieu nhat: ", soXuatHienNhieuNhat,
          "xuat hien", soLanXuatHien, "lan")


url = "F:\Desktop\python\TH2\pxu_python_TH2\input.txt"
listNumber = readFileText(url)
soChanLe(listNumber)
soNguyenTo(listNumber)
soXuatHienNhieuNhat(listNumber)
