class StudentGrade:
    """学生成绩"""

    def __init__(self, name, yuwen, shuxue):
        self.name = name
        self.yuwen = yuwen
        self.shuxue = shuxue

    def update(self, course, grade):
        if course == "语文":
            self.yuwen = grade
        elif course == "数学":
            self.shuxue = grade


xiaoming = StudentGrade("小明", 88, 99)
xiaoming.yuwen = 89
xiaoming.shuxue = 96
xiaoming.update("语文", 88)
xiaoming.update("数学", 96)
    
xiaoming = StudentGrade("小明", 88, 99)
xiaozhang = StudentGrade("小张", 87, 93)
xiaozhao = StudentGrade("小赵", 88, 90)

student_list = [xiaoming, xiaozhang, xiaozhao]
for student in student_list:
    print(student.name, student.yuwen, student.shuxue)

student_dict = {
    "小明": xiaoming,
    "小张": xiaozhang,
    "小赵": xiaozhao,
}
for name, student in student_dict.items():
    print(f"学生{name}的成绩是{student.yuwen}, {student.shuxue}")