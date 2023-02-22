"""
新建一个自己的英汉翻译词典文件“英汉翻译.txt”，复制过去，包含如下内容：
sheep,羊
tiger,老虎
duck,鸭子
fish,鱼

制作一个网页返回
URL地址设置成：/english
读取文件内容：f.read()
返回给网页前端

启动服务器
打开网页，展示词典数据
"""
from flask import Flask

app = Flask("英语词典访问")


@app.route("/english")
def show_file():
    with open("英汉翻译.txt", encoding="utf8") as f:
        cont = f.read()
        cont = cont.replace("\n", "<br/>")
        return cont


app.run()