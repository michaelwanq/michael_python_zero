"""
编写代码实现猜数字的游戏：
使用random.randint(1,100)随机生成一个数字target
循环10次，让用户猜一个数字；
如果用户的数字比target大，提示用户猜的大了，继续下一次猜测
如果用户的数字比target小，提示用户猜的小了，继续下一次猜测
如果用户猜的数字对了，恭喜用户猜对了，退出循环
如果猜了10次还没猜对，给用户展示信息“很遗憾你没猜对，正确数字是{target}”提示结果
"""
import random
target = random.randint(1,100)
i = 1
while i <= 10:
    number = input("请输入你的数字：")
    number = int(number)
    if number != target:
        print(target)
        print(f"这是第{i}次机会，你猜的数字是{number}，你猜的不对！")
        i += 1
    else:
        print(f"这是第{i}次机会，你猜的数字是{number}，你猜对了，恭喜！")
        break
print(f'i的值为：',i)
if i == 11:
    print('很遗憾，10次机会你都没猜对，欢迎你下次再来！')