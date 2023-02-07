student_grade = {}

while True:
    info = input("请输入学生姓名和成绩，用空格分割：")
    if info == "quit":
        break
    # str.split函数，可以用空白符号拆分大字符串
    name, grade = info.split()
    grade = int(grade)
    # 存入字典
    student_grade[name] = grade

print("学生信息如下：")
for name, grade in student_grade.items():
    print(name, grade)

print("最高分：", max(student_grade.values()))
print("最低分：", min(student_grade.values()))
print("平均分：", sum(student_grade.values()) / len(student_grade))