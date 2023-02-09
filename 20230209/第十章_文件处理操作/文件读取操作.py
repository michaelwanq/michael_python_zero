"""
方法一、直接读取整个文件
f = open("访客列表.txt", encoding="utf8")

content = f.read()
print(content)

f.close()

# 方法二、使用with open读取整个文件
with open('访客列表.txt',encoding='utf8') as fin:
    content = fin.read()
    print(content)

# 方法三、逐行读取
with open('访客列表.txt',encoding='utf-8') as fin:
    for line in fin:
        line = line[:-1]
        print(line)
"""
# 方法四、使用readline（）函数逐行读取
with open('访客列表.txt',encoding='utf-8') as fin:
    lines = fin.readlines()
    # print(lines,type(lines))
    for line in lines:
        print(line.rstrip())