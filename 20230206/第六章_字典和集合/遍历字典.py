# 创建一个人的信息字典
user = {"id": 123, "name": "小明", "age": 20}

# 遍历键值对
for key, value in user.items():
    print(key, value)

print('*' * 10)
# 创建多个人的成绩数据
grades = {"小明": 88, "小花": 99, "小张": 77, "小白": 85}

for name in grades.keys():
    # 可以只使用key，也可以用字典的方式获得value
    print(f"{name}的成绩是：", grades[name])
