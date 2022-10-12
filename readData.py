"""
  读取生成的数据，返回出勤表的dataframe格式。
  @author:Jin Mingqing
  update: 10/8
"""
import csv
import pandas as pd


def addHeader(input_path, output_path):
    """

    :param input_path: 生成的数据文件
    :param output_path: 增加标题行的数据文件
    :return: None
    """
    with open(input_path, 'r', newline='', encoding='utf-8') as csv_in_file:
        with open(output_path, 'w', newline='', encoding='utf-8') as csv_out_file:
            filereader = csv.reader(csv_in_file)
            filewriter = csv.writer(csv_out_file)
            header_list = ['name', 'Lesson1', 'rate1', 'Lesson2', 'rate2', 'Lesson3', 'rate3', 'Lesson4', 'rate4',
                           'Lesson5', 'rate5', 'Lesson6', 'rate6', 'Lesson7', 'rate7', 'Lesson8', 'rate8',
                           'Lesson9', 'rate9', 'Lesson10', 'rate10', 'Lesson11', 'rate11', 'Lesson12', 'rate12',
                           'Lesson13', 'rate13', 'Lesson14', 'rate14', 'Lesson15', 'rate15', 'Lesson16', 'rate16',
                           'Lesson17', 'rate17', 'Lesson18', 'rate18', 'Lesson19', 'rate19', 'Lesson20', 'rate20']
            filewriter.writerow(header_list)
            for row in filereader:
                filewriter.writerow(row)


def readAttendance(filepath):
    """

    :param filepath: 增加标题行后的文件
    :return: 将文件中数字部分去掉[、]并转换为dataframe格式
    """
    df = pd.read_csv(filepath)
    for i in range(len(df)):
        for j in range(1, 41, 2):
            df.iloc[i, j] = int(df.iloc[i, j][1])
        for k in range(2, 41, 2):
            df.iloc[i, k] = float(df.iloc[i, k][:-1])
    return df
