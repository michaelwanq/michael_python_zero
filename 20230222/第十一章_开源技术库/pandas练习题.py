"""
编写婚礼礼金录入程序，存入到Excel文件
建立datas一个列表，将来要存储成[[“小明”, 1000], [“小张”, 800]]的形式
while true循环
输入quit退出循环
输入 小明 1000，分割到姓名、金额字段，存入列表
退出循环后
创建pd.DataFrame
存入Excel文件
"""
import pandas as pd

datas = []
while True:
    message = input('请输入学生姓名和成绩：')
    if message == 'quit':
        print('感谢你的使用，再见！')
        break
    datas.append(message.split())
    print(datas)

df = pd.DataFrame(datas,
    columns=["姓名", "成绩"])

df.to_excel("成绩excel文件.xlsx")
