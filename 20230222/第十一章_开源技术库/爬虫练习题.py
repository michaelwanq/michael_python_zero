"""
练习题：
蚂蚁老师有个网站地址是 http://antpython.net/
用requests.get请求这个网页，查看状态码和结果文本
将文本存储到一个本地的电脑文件 antpython.html 文件中
打开自己的电脑文件夹 双击 antpython.html 文件，查看效果
"""
import requests

url = "http://www.antpython.net/"
r = requests.get(url)
print(r.status_code)
with open('antpython.html', 'w',encoding='utf8') as f:
    f.write(r.text)
