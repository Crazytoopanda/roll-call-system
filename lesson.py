"""
T-S-Manager课程类

@author: lfa
update: 2022/10/8
"""
import random


class Lesson(object):

    def __init__(self, lesson_id:str, lesson_name:str, lesson_stu_num:int, lesson_diff:float, lesson_mean:float):
        """
        定义课程类
        @param lesson_id: 课程id(3位)
        @param lesson_name: 课程名字
        @param lesson_stu_num: 课程学生数
        @param lesson_diff: 课程难易程度(0-1) 1为最难
        @param lesson_mean: 课程兴趣情况(0-1)
        """
        self.id = lesson_id
        self.name = lesson_name
        self.stu_num = lesson_stu_num
        self.difficult = lesson_diff
        self.mean = lesson_mean
        self.dormitories = []

    def get_avg_grade(self) -> float:
        return (1-self.difficult)*100

    def get_stand(self) -> float:
        """
        这里考虑到课程情况
        :return: 该课程的成绩标准差
        """
        return 20 * (1-abs(2*self.difficult-1))

    def get_students(self, students:list):
        self.students = students.copy()

    def get_absence_chance(self):
        """
        return: 返回学生缺课的可能值
        """
        return self.difficult - self.mean
