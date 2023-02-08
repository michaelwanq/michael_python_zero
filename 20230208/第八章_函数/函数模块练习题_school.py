"""
新建一个.py叫做 student_query.py
里面放上方的字典，提供一个函数叫做 get(name)，输入name，返回字典信息

新建第二个.py文件，叫做school.py
在文件中
编写While True循环
input可以输入用户名字
查询student_query模块
如果查询到了用户信息，展示信息
如果查询不到，说没有这个学生的信息
"""
import student_query as sq

while True:
    username = input("请输入你需要查询的用户名：")
    if username == 'quit':
        print('欢迎再次查询！')
        break
    else:
        name = sq.get(username)
        print(f'你查询的用户{username}信息是：', name)
