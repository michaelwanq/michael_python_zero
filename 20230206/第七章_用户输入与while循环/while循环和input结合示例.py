# while和input函数可以配合，实现和用户不断的交互
while True:
    fruit = input("请输入你喜欢的水果，输入quit则会退出程序：")

    if fruit == "quit":
        break
    else:
        print("很好，你喜欢这个水果：", fruit)