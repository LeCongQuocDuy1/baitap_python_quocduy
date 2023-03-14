import mysql.connector
import threading


class DbConnect(object):
    # biến lưu trữ đối tượng duy nhất - trong TH này. Nó bảo đảm lưu trữ 1 đối tượng duy nhất
    __instance = None
    # bảo đảm chỉ có duy nhất  1 luồng được truy cập vào _instance  1 lúc
    __lock = threading.Lock()

    # tạo 1 đối tượng mới - được gọi cả trước khi hàm init được gọi
    # cls là class hiện tại
    # *args(danh sách tham số không tên => tuple ) - (value, value,..)  => sum(1,2,3) => python chuyển sang kiểu tuple (1,2,3)
    # **kwargs(danh sách tham số có tên) - (key-value, key-value,...) => sum(a=1,b=2,c=3) => python chuyển sang kiểu dict {'a':1,'b':2,'c':3}
    def __new__(cls, *args, **kwargs):
        # "with" là 1 cách viết tắt của try-finally ( mở kết nối - xử lý- đóng kết nối) => giải phóng tài nguyên khi thực hiện xong
        with cls.__lock:  # bảo đảm chỉ có duy nhất  1 luồng được truy cập vào _instance  1 lúc
            if not cls.__instance:  # nếu chưa có đối tượng nào được tạo thì tạo mới
                # PT này đưuọc sử dụng để trả về đối tượng của chính nó(đối tượng hiện tại)
                cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        self.connectDb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="pxu_python_TH3"

        )

    def getConnection(self):
        return self.connectDb
