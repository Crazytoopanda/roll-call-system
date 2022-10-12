# """
# T-S-Manager课程管理类

# @author: lfa
# update: 2022/10/6
# """

# class Class_Manager(object):

#     def __init__(self, classes:dict):
#         """
#         定义类
#         @param classes: dict，键表示课程，值表示学分
#         """
#         self.classes = classes

#     def append_class(self, class_id:str, class_grade:float):
#         """
#         增加课程以及课程学分
#         @param class_name: 课程名字
#         @param class_grade: 课程学分
#         return: 空
#         """
#         self.classes[class_name] = class_grade

#     def delete_class(self, class_name:str):
#         """
#         删除课程
#         @param class_name: 课程名字
#         @return: 若有错误返回err信息，无错误返回空
#         """
#         if class_name not in self.classes.keys():
#             err = "未能找到该课程，无法删除"
#             return err
#         else:
#             self.classes.pop(class_name)
    
#     def search_class_grade(self, class_name:str):
#         """
#         寻找课程
#         @param class_name: 课程名字
#         return: 返回该课程的学分，如果不存在返回0
#         """
#         if class_name not in self.classes.keys():
#             return 0
#         else:
#             return self.classes[class_name]