"""
while不只是可以单次处理，也可以实现列表元素的处理
模拟场景：从互联网的网页上爬取数据
"""
import time

url_todo = ["url1", "url2", "url3"]
url_success = []

while url_todo:
    # pop方法，可以从List中删除一个元素并返回元素
    new_url = url_todo.pop()
    print("正在爬取URL：", new_url)
    # 程序暂停1秒钟，模拟一下从网上爬取这个网页
    time.sleep(1)
    # 记录哪些爬取过了
    url_success.append(new_url)

print("爬取完毕，待爬取URL：", url_todo)
print("爬取完毕，已爬取的URL：", url_success)
