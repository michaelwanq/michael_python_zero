numbers = range(10)
for number in numbers:
    if number == 0:
        print("当前数字是0")
    elif number % 2 == 0:
        print("发现一个偶数：", number)
    else:
        print("发现一个奇数：", number)

print("数据读取完毕")
