# pip install wheel
# pip install pandas
# pip install openpyxl
import pandas as pd


class Student:
    def __init__(self, maSV, ho, ten, ngaySinh, mToan, mLy, mHoa):
        self.maSV = maSV
        self.ho = ho
        self.ten = ten
        self.ngaySinh = ngaySinh
        self.mToan = mToan
        self.mLy = mLy
        self.mHoa = mHoa
        self.xepLoai = self.xepLoaiHocLuc()

    def mTrungBinh(self):
        return (self.mToan + self.mLy + self.mHoa) / 3

    def xepLoaiHocLuc(self):
        if self.mTrungBinh() >= 8:
            return "Gioi"
        elif self.mTrungBinh() >= 6.5:
            return "Kha"
        elif self.mTrungBinh() >= 5:
            return "Trung Binh"
        else:
            return "Yeu"

# đọc file excel


def readExcel(url):
    # đọc file excel
    # skiprows: bỏ qua n dòng đầu tiên
    # nrows: chỉ đọc n dòng
    # usecols: chỉ đọc cột 1 => 8
    # iloc[a, b] a: hàng, b: cột
    require_cols = [1, 2, 3, 4, 5, 6, 7]
    dataframe1 = pd.read_excel(
        url,  skiprows=11, nrows=51, usecols=require_cols)
    listStudent = []
    for i in range(len(dataframe1)):
        sv = Student(dataframe1.iloc[i, 0], dataframe1.iloc[i, 1], dataframe1.iloc[i, 2], dataframe1.iloc[i, 3],
                     dataframe1.iloc[i, 4], dataframe1.iloc[i, 5], dataframe1.iloc[i, 6])
        listStudent.append(sv)
    return listStudent


def SortListStudent(listStudent):
    # range(start, stop, step)
    # len: độ dài của mảng
    # i:  = start
    for i in range(len(listStudent)):
        min = i
        for j in range(i+1, len(listStudent)):
            if listStudent[min].ten > listStudent[j].ten:
                min = j
         # đổi chỗ phần tử thứ nhất với phần tử hiện tại
        listStudent[i], listStudent[min] = listStudent[min], listStudent[i]
        # lisStudentMin = listStudent[i]
        # listStudent[i] = listStudent[min]
        # listStudent[min] = lisStudentMin
    return listStudent

# in ra danh sách sinh viên


def printListStudent(listStudent):
    # in ra danh sách sinh viên sau khi sắp xếp
    for i in range(len(listStudent)):
        print(listStudent[i].maSV, listStudent[i].ho, listStudent[i].ten,
              listStudent[i].ngaySinh, listStudent[i].mTrungBinh(), listStudent[i].xepLoai)

# thống kê bao nhiêu sinh viên giởi, khá, trung bình, yếu


def statistical(listStudent):
    countGioi = 0
    countKha = 0
    countTB = 0
    countYeu = 0
    for i in range(len(listStudent)):
        if listStudent[i].xepLoai == "Gioi":
            countGioi += 1
        elif listStudent[i].xepLoai == "Kha":
            countKha += 1
        elif listStudent[i].xepLoai == "Trung Binh":
            countTB += 1
        else:
            countYeu += 1

    print("So sinh vien gioi: ", countGioi)
    print("So sinh vien kha: ", countKha)
    print("So sinh vien trung binh: ", countTB)
    print("So sinh vien yeu: ", countYeu)


url = 'F:\Desktop\python\TH2\pxu_python_TH2\input.xlsx'
listStudent = readExcel(url)
listStudent = SortListStudent(listStudent)
printListStudent(listStudent)
statistical(listStudent)
