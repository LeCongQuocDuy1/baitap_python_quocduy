import mysql.connector
import StudentService

stuserv= StudentService
check = -1
stuserv.sqlconn()
while check != 0:
    print("1. Doc f3ile excel ")
    print("2. Xem danh sách sinh viên")
    print("3. In ra Mysql")
    check = int(input("Nhập số: "))
    while check < 0 or check > 3:
        check = int(input("Nhập lại số: "))

    print("*" * 50)
    if check == 1:
        stuserv.readexcel()
    elif check == 2:
        stuserv.showsv(stuserv.getlistSV())
    elif check == 3:
        stuserv.insertall(stuserv.getlistSV())
    else:
        break

    print("*" * 50)