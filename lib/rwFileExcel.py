import pandas as pd

# đọc file excel


def readExcel(url, obj):
    # đọc file excel
    # skiprows: bỏ qua n dòng đầu tiên
    # nrows: chỉ đọc n dòng
    # usecols: chỉ đọc cột 1 => 8
    # iloc[a, b] a: hàng, b: cột
    requireCols = [1, 2, 3, 4, 5, 6, 7]
    dataFrame = pd.read_excel(
        url,  skiprows=11, nrows=51, usecols=requireCols)
    listStudent = []
    for i in range(len(dataFrame)):
        sv = obj(dataFrame.iloc[i, 0], dataFrame.iloc[i, 1], dataFrame.iloc[i, 2], dataFrame.iloc[i, 3],
                 dataFrame.iloc[i, 4], dataFrame.iloc[i, 5], dataFrame.iloc[i, 6])
        listStudent.append(sv)
    return listStudent
