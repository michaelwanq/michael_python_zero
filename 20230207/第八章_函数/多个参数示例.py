# def introduce(name, gender):
#     """
#     幼儿园自我介绍
#     """
#     print(f"大家好，我的名字是：{name}，是个小{gender}")
#
#
# # 需要按顺序提供参数，顺序不能乱
# # 这叫做位置实参，按位置提供
# introduce("小明", "男生")
# introduce("小白", "女生")

def introduce(name, gender, age=6):
    """
    幼儿园自我介绍
    """
    print(f"大家好，我的名字是：{name}，是个小{gender}，今年{age}岁了")


# 调用函数时，默认参数可以不写值

# 如果不设置age，那么就是6岁
introduce("小明", "男生")

# 可以传递一个新值，覆盖默认值
introduce("小白", "女生", 5)
