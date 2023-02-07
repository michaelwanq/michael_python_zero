"""
字典的value是列表，表达每个人列表类型信息
如下是学生的爱好数据，实现代码，输出爱好名字的去重后的列表
"""
students = {
    "xiaozhang": ["足球", "篮球"],
    "xiaowang": ["篮球", "乒乓球"],
    "xiaoli": ["篮球", "棒球", "台球"],
    "xiaozhao": ["乒乓球", "羽毛球"],
}
loves = set()
for name, love in students.items():
    for l in love:
        loves.add(l)
print('学生的爱好包括：', loves)
