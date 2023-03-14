from DAO.interface.IStudentDAO import IStudentDAO
import lib.connectionDB as db
from datetime import datetime


class StudentDAO(IStudentDAO):
    def __init__(self):
        dbConnection = db.DbConnect()
        self.cnx = dbConnection.getConnection()
        self.cursor = self.cnx.cursor()

    def insert(self, student):
        sql = "Insert into Students(MaSinhVien, HoVaTen, NgaySinh, DToan, DLy, MHoa, XepLoai) values(%s,%s,%s,%s,%s,%s,%s)"
        val = (student.maSV, f"{student.ho} {student.ten}", datetime.strptime(student.ngaySinh,
               '%d/%m/%Y'), student.mToan, student.mLy, student.mHoa, student.xepLoai)
        self.cursor.execute(sql, val)
        self.cnx.commit()
        return self.cursor.lastrowid  # lấy id của bản ghi vừa insert

    def update(self, student):
        sql = "Update Students set HoVaTen = %s, NgaySinh = %s, DToan = %s, DLy = %s, MHoa = %s, XepLoai = %s where MaSinhVien = %s"
        val = (f"{student.ho} {student.ten}", datetime.strptime(student.ngaySinh, '%d/%m/%Y'),
               student.mToan, student.mLy, student.mHoa, student.xepLoai, student.maSV)
        self.cursor.execute(sql, val)
        self.cnx.commit()
        return self.cursor.lastrowid

    def delete(self, id):
        sql = "Delete from Students where MaSinhVien = %s"
        val = (id,)
        self.cursor.execute(sql, val)
        self.cnx.commit()

    def getById(self, id):
        sql = "Select * from Students where MaSinhVien = %s"
        val = (id,)
        self.cursor.execute(sql, val)
        result = self.cursor.fetchone()
        return result

    def getAll(self):
        sql = "Select * from Students"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result
