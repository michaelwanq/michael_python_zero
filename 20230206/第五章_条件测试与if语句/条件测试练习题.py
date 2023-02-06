"""
给定一个成绩grade，例如你设定一个值，例如70分；

用print输出如下条件测试：

是否及格：大于等于60分则是及格
是否不及格：小于60分则是不及格
是否满分：等于100分则是满分
是否不是满分：不等于100分，就不是满分
判断属于（优秀、中等、良好）中的中等成绩：判断是否大于等于70分并且小于90分
判断成绩数字是否很顺口：成绩等于66分、或者成绩等于88分、或者成绩等于99分
判断成绩及格并且是否是0结尾：判断成绩大于等于60，并且为60/70/80/90/100中的一个
"""
grade = int(input("请输入你本次考试的成绩："))
if grade == 100:
    print("太棒了，你考了满分！")
elif grade >= 60:
    print(f"你的成绩合格，分数为:", grade)
else:
    print(f"很遗憾，你的成绩不合格。你的成绩是：", grade)

grade = int(input("请输入你本次考试的成绩："))
if grade != 100:
    print("你的成绩还需要努力，你的分数是：", grade)

print("*" * 10)
grade = int(input("请输入你本次考试的成绩："))
if grade >= 90:
    print("你的成绩属于优秀，分数是：", grade)
elif grade >= 70 and grade < 90:
    print("你的成绩属于中等，分数是：", grade)
elif grade >= 60 and grade < 70:
    print("你的成绩刚合格，分数是：", grade)
else:
    print("你的成绩不合格，分数是：", grade)

print("*" * 10)
grade = int(input("请输入你本次考试的成绩："))
decade = int(grade / 10)
unit = grade % 10
print(decade,unit)
if decade == unit:
    print("你的成绩很顺口，分数是：", grade)
else:
    print("你的分数是：", grade)

print("*" * 10)
grade = int(input("请输入你本次考试的成绩："))
number = grade % 10
if grade >= 60 and number == 0:
    print("你的成绩合格，且为10的整数倍。你的分数是：", grade)
