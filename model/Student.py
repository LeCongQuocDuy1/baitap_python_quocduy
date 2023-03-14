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
