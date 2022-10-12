"""
T-S-Manager生成数据类

@author: lfa
update: 2022/10/8
"""

import random
import numpy as np
from faker import Faker
from student import Student
from lesson import Lesson
from dormitory import Dormitory

class Spawn_data(object):

    def __init__(self, students_num: int, lesson_num: int):
        """
        定义类
        @param students_num: 学生数量
        @param lesson_num: 课程数量
        """
        self.stu_num = students_num
        self.les_num = lesson_num
        self.lessons = []

    def add_lesson(self, lesson: Lesson):
        """
        增加课程
        :param lesson:课程信息
        :return: 空
        """
        self.lessons.append(lesson)
        return

    def spawn_dormitory(self, lesson:Lesson, dormitory_volume=3):
        """
        生成宿舍
        @param dormitory_volume: 宿舍可容纳数(3)
        """
        dorm_list = []
        dorm_num = int(self.stu_num / dormitory_volume)
        for i in range(dorm_num):
            dorm_list.append(Dormitory("{:04d}".format(i),
                dormitory_volume, random.uniform(0, 1)))  # 随机生成宿舍关系 ~~可以先生成学生并定义性格，来生成宿舍情况~~
        lesson.dormitories = dorm_list.copy()

    def spawn_lesson_students(self, lesson: Lesson, stu_avg_grade: float, stu_stand: float, often_absence_num:int):
        """
        为课程生成学生，按照学生数量进行生成
        :param lesson: 课程信息
        :return:
        """
        fake = Faker("zh_CN")
        stu_grade = np.random.normal(stu_avg_grade, stu_stand, self.stu_num)  # 学生成绩正态分布随机生成
        stu_list = []
        name_repeat = []
        for i in range(self.stu_num):
            stu = None
            fname = None
            while(True):
                fname = fake.name()
                if fname not in name_repeat:
                    break
            name_repeat.append(fname)
            if i < often_absence_num:
                stu = Student(lesson.id + "{:03d}".format(i), fname, 1)
            else:
                stu = Student(lesson.id + "{:03d}".format(i), fname)
            stu_list.append(stu)
            stu.get_grade(lesson, stu_grade[i])
        random.shuffle(stu_list)
        lesson.get_students(stu_list)

        self.spawn_dormitory(lesson) # 生成宿舍
        count = 0
        for stu in stu_list:
            if not lesson.dormitories[count].append_dorm_student(stu):
                count += 1
                lesson.dormitories[count].append_dorm_student(stu)
        self.lessons.append(lesson)
        return

    def spawn_lesson(self, lesson_id: str, lesson_name: str, diff: float, interest: float) -> Lesson:
        lesson = Lesson(lesson_id, lesson_name, self.stu_num, diff, interest)
        self.spawn_lesson_students(lesson, lesson.get_avg_grade(), lesson.get_stand(), random.randint(5, 8)) # 5-8人是惯犯
        return lesson

    def get_lesson_students_info(self, lesson:Lesson, choose:str) -> list:
        if choose == "name":
            return [i.name for i in lesson.students]
        elif choose == "id":
            return [i.id for i in lesson.students]
        elif choose == "grade":
            return [i.grades[lesson] for i in lesson.students]

    def get_dorm_info(self, lesson:Lesson, choose:str):
        if choose == "id":
            return [i.dormitory_id for i in lesson.dormitories]
        elif choose == "id:relationship":
            return {i.dormitory_id:i.relationship for i in lesson.dormitories}
        elif choose == "name:relationship":
            return {[j.name for j in i.students]:i.relationship for i in lesson.dormitories}

    def calc_les_stu_absence(self, lesson:Lesson) -> list:
        sort_list = []
        for stu in lesson.students:
            sort_list.append(stu.calc_absence_chance(lesson))
        return sort_list

    def random_choose_stu_absence(self, sort_stu_list, random_num=2) -> list:
        prefix = 0
        for i, j in sort_stu_list:
            if j == 0:
                break
            prefix += 1
        for i in range(2):
            k = random.randint(prefix, len(sort_stu_list)-1)
            sort_stu_list[k] = [sort_stu_list[k][0], 1]
        return sort_stu_list


    def define_absence_return(self, lesson:Lesson, absence_sum) -> list:
        sort_stu_list = self.calc_les_stu_absence(lesson)
        sort_stu_list = sorted(sort_stu_list, key=lambda x:x[1], reverse=True).copy()
        return_list = []
        count = 0
        for i in range(len(sort_stu_list)):
            if sort_stu_list[i][1] != 100:
                count += 1
            if count >= absence_sum:
                return_list.append([sort_stu_list[i][0], 0])
            else:
                return_list.append([sort_stu_list[i][0], 1])
        return return_list.copy()

    def to_csv(self, loc:str, stu_dict:dict):
        with open(loc, "w", encoding="utf-8") as fs:
            for key, value in stu_dict.items():
                fs.write(str(key))
                for t in value:
                    fs.write(","+str(t))
                fs.write("\n")

if __name__ == "__main__":
    class_num = 5
    every_class_student_num = 90
    iterate_time = 20
    absence_num = 4

    # 创建生成数据类
    SDM = Spawn_data(every_class_student_num, class_num)
    lesson_id = ["001", "002", "003", "004", "005"]
    lesson_name = ["软件工程", "高等数学", "机器学习", "大学英语", "数据结构"]
    lesson_diff = [0.5, 0.8, 0.6, 0.3, 0.75]
    lesson_interest = [1, 0.6, 0.3, 0.5, 0.2]
    prefix = "./PythonCode/T-S-Manager/datasets/"
    write_file = ["data_sw.csv", "data_math.csv", "data_ml.csv", "data_en.csv", "data_ds.csv"]

    # 遍历生成数据，5种课程，每节课20次，且每种课程90人
    lessons = []
    for i in range(class_num):
        
        # SDM类生成课程
        lessons.append(SDM.spawn_lesson(lesson_id[i], lesson_name[i], lesson_diff[i], lesson_interest[i]))
        stu_dict = {}
        # 20次课程上课
        for j in range(iterate_time):
            # define_absence_return表示返回该课程的学生缺席情况，可传参课程以及缺席人数
            stu_list = SDM.define_absence_return(lessons[i], absence_num+random.randint(-1, 1))
            # 将stu_list[Student, float]转成<Student.name:[float, float]>字典，以便以字符串导入 
            for stu, k in stu_list:
                if stu.name not in stu_dict.keys():
                    stu_dict[stu.name] = [[k, stu.calc_absence_chance(lessons[i])[1]]]
                else:
                    stu_dict[stu.name].append([k, stu.calc_absence_chance(lessons[i])[1]])
            # 将stu_dict写入write_file(str)文件中
            SDM.to_csv(prefix+write_file[i], stu_dict)