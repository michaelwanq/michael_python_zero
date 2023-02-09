"""
新建一个文件，叫做 英汉词典.txt
每行是一个中英文对照，逗号分隔
例如：
sheep,羊
tiger,老虎
duck,鸭子
fish,鱼
用python读取文件，建立一个字典
key是英语词语，value是汉语词语
编写while循环
输入quit退出循环
输入英语，返回汉语
如果不存在，说没有这个词语
"""
animal_dict = {}
with open("英汉词典.txt",encoding="utf8") as f:
    # lines = ec.readlines()
    # # print(lines)
    # for line in lines:
    #     if len(line.rstrip().split(',')) == 2:
    #         e_words,c_words = line.rstrip().split(',')
    #         animal_dict[e_words] = c_words
    #     else:
    #         continue
    for line in f:
        if len(line.split(',')) != 2:
            continue
        else:
            e_words, c_words = line.rstrip().split(',')
            animal_dict[e_words] = c_words
# print(animal_dict)
while True:
    words = input('请输入你想要查询的单词：')
    if words == 'quit':
        print("欢迎再次查询，再见！")
        break
    elif words in animal_dict.keys():
        print(f'你输入的{words}的翻译为：',animal_dict[words])
    else:
        print(f'无法查询到你输入的单词{words}，请重新输入！')