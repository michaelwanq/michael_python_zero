"""
学生成绩录入与保存程序
新建代码“成绩录入json.py”
加载文件的词典文件：json.txt
如果文件存在，加载到字典 grade_dict
如果文件不存在，新建一个成绩字典，例如grade_dict = {}
while true，输入多个成绩
每行成绩，形如“小明 80”、“小李 90”
使用str.split拆分成name和grade
存入字典中，name是Key，grade是Value
输入quit，退出循环
将grade_dict更新保存到json文件中：json.txt
类似用f.write(json.dumps(grade_dict))即可
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
    info = input("请输入姓名和成绩：")
    if info == "quit":
        break
    fields = info.split()
    if len(fields) != 2:
        continue
    name, grade = fields
    grade = int(grade)
    grade_dict[name] = grade

with open(file_name, "w", encoding="utf8") as f:
    f.write(json.dumps(grade_dict))