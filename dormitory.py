"""
T-S-Manager宿舍类

@author: lfa
update: 2022/10/8
"""

class Dormitory(object):

    def __init__(self, id:str, capacity:int, relationship:float):
        """
        定义宿舍类
        @param id: 宿舍id(4位)
        @param capacity: 宿舍可容纳量
        @param relationship: 宿舍关系情况(0-1):越高影响舍友一起不想上课
        """
        self.dormitory_id = id
        self.capacity = capacity
        self.students = []
        self.relationship = relationship
    
    def change_dorm_relationship(self, relationship:float):
        self.relationship = relationship

    def append_dorm_student(self, student) -> int:
        """
        为该宿舍添加学生
        @param student: 学生
        return: 返回0：不可以添加；返回1：可以添加
        """
        if self.capacity == 0:
            return 0
        else:
            self.students.append(student)
            student.get_dorm(self)
            self.capacity -= 1
            return 1
