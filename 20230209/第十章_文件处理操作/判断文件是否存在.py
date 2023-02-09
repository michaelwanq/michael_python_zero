import os
file_path1 = r"D:\python\michael_python_zero\20230209\第十章_文件处理操作\数字列表.txt"
file_path2 = r"D:\python\michael_python_zero\20230209\第十章_文件处理操作\数字列表2.txt"
if os.path.exists(file_path1):
    print('查询到你要找的对象：',file_path1)
else:
    print('无法查询到你要找的对象')

if os.path.exists(file_path2):
    print('查询到你要找的对象：数字列表2.txt')
else:
    print('无法查询到你要找的对象：',file_path2)