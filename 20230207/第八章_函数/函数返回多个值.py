students = {
    "xiaoming": {"id": 101, "age": 18, "gender": "boy"},
    "xiaohuang": {"id": 102, "age": 19, "gender": "girl"},
    "xiaowang": {"id": 103, "age": 17, "gender": "girl"},
}


def get_student(name):
    """
    加法函数，也可以自动处理字符串类型
    """
    if name in students:
        return students[name]["age"], students[name]["gender"]
    else:
        return None, None


# 可以分开变量接收
age, gender = get_student("xiaohuang")
print(f'xiaohuang是一位{age}岁的{gender}。')
# 可以单个变量接收，这个时候info是一个元组
info = get_student("xiaoxiaoxiao")
print(type(info))
