## 示例一、列表中嵌套字典
# 学生信息字典的列表，表达很多个学生信息
# students = [
#     {"id": 101, "name": "xiaozhang", "grade": 88},
#     {"id": 102, "name": "xiaowang", "grade": 99},
#     {"id": 103, "name": "xiaoli", "grade": 77},
#     {"id": 104, "name": "xiaozhao", "grade": 86},
# ]
#
# for student in students:
#     id, name, grade = student["id"], student["name"], student["grade"]
#     print(f"学号为{id}的姓名是{name}，成绩是{grade}分")

## 示例二、字典中嵌套字典
students = {
    "xiaozhang": {"id": 101, "grade": 88},
    "xiaowang": {"id": 102, "grade": 99},
    "xiaoli": {"id": 103, "grade": 77},
    "xiaozhao": {"id": 104, "grade": 86}
}
for name, info in students.items():
    id, grade = info["id"], info["grade"]
    print(f"姓名为{name}，学号为{id}，成绩是{grade}分。")
