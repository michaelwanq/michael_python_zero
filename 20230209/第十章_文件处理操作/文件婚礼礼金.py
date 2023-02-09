"""
改进婚礼礼金程序

用”w”模式，打开一个文件“婚礼礼金.txt”文件
写一个while true
请输入“姓名 礼金”，例如“小明 1000”
将数据存储到文件中，每行一个数据
输入quit退出循环

退出循环后
重新读取文件，按行读取
把礼金读取到list中
输出list的统计数据，加和、最高、最低、平均值

"""

fname = "婚礼礼金.txt"

with open(fname, "w", encoding="utf8") as f:
    while True:
        print("#"*20)
        info = input("请输入来人和金额：")
        if info == "quit":
            break
        fields = info.split()
        if len(fields) == 2:
            name, money = fields
        else:
            continue
        money = int(money)
        f.write(f"{name},{money}\n")

with open(fname, encoding="utf8") as f:
    moneys = []
    for line in f:
        line = line[:-1]
        fields = line.split(",")
        if len(fields) == 2:
            name, money = fields
        else:
            continue
        moneys.append(int(money))

    # 加和、最高、最低、平均值
    print("加和:", sum(moneys))
    print("最高:", max(moneys))
    print("最低:", min(moneys))
    print("平均值:", sum(moneys) / len(moneys))