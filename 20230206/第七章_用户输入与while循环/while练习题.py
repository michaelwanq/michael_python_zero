"""
简单的快递运费计算程序（来自真实的需求）：
用户可以输入物品的重量，程序可以计算快递的价格
该程序需要一直运行，直到用户输入quit可以退出程序
根据不同的重量，输出不同的价格，计算逻辑如下
"""
while True:
    message = input("请输入你要寄的快递重量：")
    # print('输入的重量是：',weight)
    if message == 'quit':
        print("感谢你的使用，欢迎再次光临！")
        break
    else:
        weight = float(message)
        if 0 < weight <= 1:
            print(f"你的快递重量是{float(message)}kg，快递费用是7元。")
        elif 1 < weight <= 3:
            print(f"你的快递重量是{weight}kg，快递费用是{7 + 2 * (weight - 1)}元。")
        elif weight > 3:
            print(f"你的快递重量是{weight}kg，快递费用是{7 + 3 * (weight - 3)}元。")
        else:
            print('你输入的数字是0或者负数！',weight)
