"""
  运用点名算法对五门课程的所有课进行点名，输出最终的E值
  @author:Jin Mingqing
  update: 10/8
"""
from Roll_call import *
from readData import *
import os


if __name__ == "__main__":
    prrefix = "./PythonCode/T-S-Manager/datasets/"
    course = ['data_ds.csv', 'data_en.csv', 'data_math.csv', 'data_ml.csv', 'data_sw.csv']
    Count = 0
    Count_absence = 0
    for i in range(0, 5):
        prefix = os.path.splitext(course[i])[0]
        suffix = os.path.splitext(course[i])[-1]
        file_modified = prefix + str(1) + suffix
        addHeader(prrefix+course[i], prrefix + file_modified)
        Df = readAttendance(prrefix+file_modified)
        count, count_absence = roll_call(Df)
        Count += count
        Count_absence += count_absence
    print(" 总点名数：{:}".format(Count))
    print(" 有效请求数：{:}".format(Count_absence))
    print("E={:.6f}".format(Count_absence / Count))
