"""
怎样计算1~100的数字的和
"""
number, sum_value = 0, 0

while True:
    number += 1

    # 奇数，跳过，不计算
    if number % 2 == 1:
        continue

    sum_value += number

    # 如果已经超过100了，结束循环
    if number > 100:
        break

print(sum_value)
