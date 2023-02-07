"""
编写一个函数：
名字叫做 sum_numbers
有一个参数叫做 number
函数内，实现 1~number 之间，所有数字的加和
打印加和的结果
调用多次这个函数，传入不同的number查看结果
"""


def sum_numbers(number):
    ## 方法一
    # numbers = number
    # total = 0
    # if numbers > 1:
    #     for i in range(1, numbers + 1):
    #         total = i + total
    #     print("你输入的数字是：", number)
    #     print("sum =", total)
    # elif numbers == 1:
    #     print('你输入的数字是1，所有数字之和是1。')
    # else:
    #     print("你输入的数字格式有问题，请重新输入！")
    ##方法二、更简洁
    sum_values = 0
    for i in range(1,number+1):
        sum_values += i
    print(f'{number}加和的结果是：',sum_values)
while True:
    your_number = input("请输入你的数字：")
    if str(your_number).isnumeric():
        number = int(your_number)
        sum_numbers(number)
        break
    else:
        print('你输入不是数字，请重新输入')
        continue