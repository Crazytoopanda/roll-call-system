"""
T-S-Manager课程学生类

@author: lfa
update: 2022/10/6
"""
import random

import numpy as np
from dormitory import Dormitory
from lesson import Lesson

class Student(object):

    def __init__(self, id:str, name:str, often_absence=0):
        """
        定义类
        @param id: 该学生id(3位)
        @param name: 该学生姓名
        @param dorm: 该学生所属宿舍
        """
        self.id = id
        self.name = name
        self.grades = {}
        self.nature = random.uniform(0, 1)
        self.often_absence = often_absence
        
    def get_dorm(self, dormitory:Dormitory):
        self.dorm = dormitory

    def get_grade(self, lesson:Lesson, grade:float):

        self.grades[lesson] = grade
        self.judge_grade_valid(lesson)

    # def return_classes(self) -> list:
    #     return list(self.grade.keys())

    # def sum_choice_grades(self, choice_grades:list) -> float:
    #     """
    #     求和所选课程的学分
    #     @param choice_grades: 所选课程
    #     """
    #     sum_grade = 0.0
    #     for i in choice_grades:
    #         sum_grade += self.grades[i]
    #     return sum_grade/len(choice_grades)

    def judge_grade_valid(self, lesson:Lesson):
        if self.grades[lesson] > 100:
            self.grades[lesson] = 100
        elif self.grades[lesson] < 0:
            self.grades[lesson] = 0

    def update_nature(self):
        return random.uniform(0, 1)

    def calc_absence_chance(self, lesson:Lesson) -> list:
        self.absence_prob = (1-self.grades[lesson]/100)*abs(2*self.dorm.relationship-1) \
                + lesson.get_absence_chance() + self.nature
        self.nature = self.update_nature()
        if self.often_absence == 1:
            if random.randint(1, 5) != 2:
                return [self, 100]
        return [self, self.absence_prob]
