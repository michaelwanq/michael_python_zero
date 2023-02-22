"""
升级成绩录入程序：
while true录入姓名和成绩，存入“学生成绩带异常处理.txt”文件
增加成绩不是数字的异常处理
如果输入内容抛异常，不要暂停程序；
提示用户“发生的异常是什么”
提示“当前的信息是什么，继续可以继续录入”
"""
import os
import json

file_name = "成绩录入json.txt"
grade_dict = {}
if os.path.exists(file_name):
    with open(file_name, encoding="utf8") as f:
        grade_dict = json.loads(f.read())

print("### 读取文件后的内容")
for key, value in grade_dict.items():
    print(key, value)

while True:
    print("#" * 20)
    try:
        info = input("请输入姓名和成绩：")
        if info == "quit":
            break
        fields = info.split()
        if len(fields) != 2:
            continue
        name, grade = fields
        grade = int(grade)
        grade_dict[name] = grade
    except ValueError as e:
        print('你输入的成绩不是整数：',e)
        continue

with open(file_name, "w", encoding="utf8") as f:
    f.write(json.dumps(grade_dict))
