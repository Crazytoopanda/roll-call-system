"""
  Implement the roll call algorithm.
  @author:Jin Mingqing
  update: 10/8
"""


def roll_call(df):
    stu_absence = []
    count = 0
    count_absence = 0

    for j in range(1, 41, 2):
        # 先对优先级100的学生进行点名
        for x in range(len(stu_absence)):
            if df.iloc[x, j] == 1:
                count_absence += 1
            count += 1

        for i in range(len(df)):
            # 跳过已点名的优先级的学生
            flag_stu_repetition = 0
            for y in range(len(stu_absence)):
                if i == stu_absence[y]:
                    flag_stu_repetition = 1
                    break
            if flag_stu_repetition == 1:
                continue
            # 选择本次上课优先级为100的学生进行点名，并添加到优先级100的学生列表
            if df.iloc[i, j+1] == 100:
                stu_absence.append(i)
                if df.iloc[i, j] == 1:
                    count_absence += 1
                count += 1
        # print(stu_absence)
    return count, count_absence
