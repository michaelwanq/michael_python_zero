"""
输入一个目标数字，例如8
用代码查找，哪些数字加和等于8，例如2和6、3和5、7和1、4和4；
注意：如果5和3已经出现了一对，不要再出现3和5，只是一回事

提示：用两次for循环这个列表，即可实现
"""
numbers = [2, 3, 5, 8, 7, 4, 1, 6]
target = 8

result = []
for a in numbers:
    for b in numbers:
        # print(a, b)
        if a + b == target and (a, b) not in result:
            print(f"找到了一对数字：{a} + {b} == {target}")
            result.append((a, b))
            result.append((b, a))
print(result)
