"""
新建一个python文件，叫做判断 “文件路径是否存在.py”

当前目录下新建一个txt文件，叫做 “文件路径是否存在.txt”
用os.path.exists方法，输出这个文件是否存在

在当前目录新建一个子目录，叫做“文件路径是否存在”，在目录中新建一个文件叫“测试路径.txt”
用os.path.exists方法，自己编写这个文件的路径，判断是否存在

在pycharm中，文件路径是否存在.txt 这个文件上，右键，复制路径，复制绝对路径
用反斜线的方式得到文件路径，自己加r前缀，用os.path.exists方法，输出这个文件是否存在

随便写一个文件名字，用os.path.exists方法，输出这个文件是否存在
"""
import os
# file_path1 = 文件路径是否存在.txt
# file_path2 = 文件路径是否存在
while True:
    path = input('你想要查找的目标是：')
    if path == 'quit':
        print('欢迎再次查询，再见！')
        break
    else:
        if os.path.exists(path):
            if os.path.isdir(path):
                print(f'你要查找的目录：{path}，确定存在')
            else:
                print(f'你要查找的文件：{path}，确定存在')
        else:
            print(f'你要查找的文件：{path}，确定不存在！')