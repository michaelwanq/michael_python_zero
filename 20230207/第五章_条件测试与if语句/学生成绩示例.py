# 学生成绩
grades = [66, 55, 75, 80, 43, 90]

for grade in grades:
    print("** 你的成绩是：", grade)
    if grade >= 60:
        print("恭喜你，通过了考试")
    else:
        print("很遗憾，你的成绩不及格")
        print("请继续努力")

grade = 70
print(grade in grades)
print(grade > 60)