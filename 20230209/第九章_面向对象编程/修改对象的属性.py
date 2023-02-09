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
print(xiaoming.yuwen)
print(xiaoming.shuxue)