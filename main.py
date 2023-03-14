import model.Student as student
import lib.rwFileExcel as rw
import DAO.StudentDAO as studentDAO


class main:
    def __init__(self):
        self.student_dao = studentDAO.StudentDAO()
        pass

    def getStudentById(self, id):
        stu = self.student_dao.getById(id)
        print(stu)

    def getAllStudent(self):
        listStudent = self.student_dao.getAll()
        for stu in listStudent:
            print(stu)

    def insertStudent(self, student):
        self.student_dao.insert(student)

    def updateStudent(self, student):
        self.student_dao.update(student)

    def deleteStudent(self, id):
        self.student_dao.delete(id)

    def readExcel(self, url, obj):
        listStudent = rw.readExcel(url, obj)
        for i in range(len(listStudent)):
            print(listStudent[i].maSV, listStudent[i].ho, listStudent[i].ten,
                  listStudent[i].ngaySinh, listStudent[i].mTrungBinh(), listStudent[i].xepLoai)


obj = main()
# obj.getAllStudent()
# obj.getStudentById('B17DCCN001')

# insert data
# student = student.Student('B17DCCN001', 'Nguyễn Văn',
#                           'A', '01/01/2000', 10, 10, 10)
# obj.insertStudent(student)


# update data
student = student.Student('B17DCCN001', 'Nguyễn Văn',
                          'C', '01/01/2000', 10, 10, 10)
obj.updateStudent(student)

# delete data
# obj.deleteStudent('B17DCCN001')

# read data from excel
# url = 'C:\Users\Administrator\Downloads\python_bt3-4-main\baitap3_quocduy\input.xlsx'
# objType = student.Student
# obj.readExcel(url, objType)
