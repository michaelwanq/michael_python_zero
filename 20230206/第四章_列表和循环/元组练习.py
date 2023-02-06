"""
完成如下代码：
新建一个元组，叫student，信息有学号/姓名/年龄/身高，内容有(1001, 'xiaoming', 20, 176)
使用for循环，遍历student的各个元素
使用变量拆包的方式，得到学号/姓名/年龄/身高多个变量，打印结果
修改姓名这个元素，变成daming，会发现报错不允许修改
只能整体修改student，例如设置为新的学生信息(1002, 'xiaobai', 21, 173)
"""
student = (1001, 'xiaoming', 20, 176)
print(f'元组列表信息是：',student)
# 对元组列表进行遍历
for message in student:
    print(message)

学号,姓名,年龄,身高 = student
print(f'学号是：',学号)
print(f'学号是：',姓名)
print(f'学号是：',年龄)
print(f'学号是：',身高)

student = (1002, 'xiaoming', 21, 177)
print(student)

