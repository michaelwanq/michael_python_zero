"""
求余数练习题：
使用input，提示让用户输入一个数字
将输入变成数字类型
计算是奇数还是偶数，给用户展示结果
"""
number = int(input('请输入你想要判断的数字：'))
if number == 0:
    print('你输入的数字是0！')
elif number % 2 == 1:
    print(f'你输入的数字{number}是奇数。')
else:
    print(f'你输入的数字{number}是偶数。')
