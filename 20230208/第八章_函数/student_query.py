students = {
    "xiaoming": {"id": 101, "age": 18, "gender": "boy"},
    "xiaohuang": {"id": 102, "age": 19, "gender": "girl"},
    "xiaowang": {"id": 103, "age": 17, "gender": "girl"},
}


def get(name):
    ## 方法一、自己的代码
    # if name in students:
    #     return students[name]
    # else:
    #     return '你查询的用户不存在！'
    ## 方法二、查询字典中没有的键，会返回none这个值，可直接借用这个返回值！
    return students.get(name)

# print(f"xiaoming的个人信息是{get('xiaoming')}。")
