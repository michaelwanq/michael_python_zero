"""
给定一个年龄age，例如数字20
做如下判断语句的编写：
如果小于13岁，打印“小孩”
如果大于等于13，并且小于18岁，打印“青少年”
如果大于等于18，并且小于65岁，打印“成年人”
如果大于等于65岁，打印“老年人”
"""
# 格式化代码  ctrl + alt + l
# 万能提示    alt + enter
while True:
    message = input("是否退出当前判断？如果退出，请输入'quit':")
    if message == 'quit':
        break
    else:
        age = int(input("请输入你要判断的年龄："))
        if age < 13:
            print("小孩")
        elif age >= 13 and age < 18:
            print("青少年")
        elif age >= 18 and age < 65:
            print("成年人")
        else:
            print("老年人")

