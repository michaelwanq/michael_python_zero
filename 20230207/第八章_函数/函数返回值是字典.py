students = {
    "xiaoming": {"id": 101, "age": 18, "gender": "boy"},
    "xiaohuang": {"id": 102, "age": 19, "gender": "girl"},
    "xiaowang": {"id": 103, "age": 17, "gender": "girl"},
}


# def get_student(name):
#     if name in students:
#         return students[name]
#     else:
#         return None
#
#
# print(get_student("xiaohuang"))
# print(get_student("xiaoxiaoxiao"))
name = 'xiaowang'
if name in students:
    print(name)
else:
    print("找不到你输入的用户名！",name)