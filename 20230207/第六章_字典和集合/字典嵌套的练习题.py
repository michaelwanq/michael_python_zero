"""
# 学生信息字典的列表，表达很多个学生信息
students = {
    "xiaozhang": {"id": 101, "grade": 88},
    "xiaowang": {"id": 102, "grade": 99},
    "xiaoli": {"id": 103, "grade": 77},
    "xiaozhao": {"id": 104, "grade": 86},
}
实现如下效果：
将xiaoli的成绩，从77分改成87分
将所有grade放到一个列表里，叫做grades
将grades降序排列后输出
"""
students = {
    "xiaozhang": {"id": 101, "grade": 88},
    "xiaowang": {"id": 102, "grade": 99},
    "xiaoli": {"id": 103, "grade": 77},
    "xiaozhao": {"id": 104, "grade": 86},
}

# 将xiaoli的分数从77改为87
# students["xiaoli"] = {"id": 101, "grade": 87}
students["xiaoli"]["grade"] = 87
print(f'xiaoli的学号是：',students['xiaoli']['id'])
info = students['xiaoli']
print(f"xiaoli的学号是{info['id']}，成绩是{info['grade']}")

# 将所有grade放到一个列表里，叫做grades，将grades降序排列后输出
grades = []
for name,info in students.items():
    grade = info['grade']
    grades.append(grade)

print('所有学生的成绩列表：',grades)
print('所有学生的信息如下：',students)
reverse_grades = sorted(grades,reverse=True)
print('所有学生的逆序排列列表为：',reverse_grades)

