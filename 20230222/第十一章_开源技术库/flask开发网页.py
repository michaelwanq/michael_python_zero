from flask import Flask

app = Flask("我的网页")


@app.route("/index")
def index():
    return "这是我的网页，michael!"


app.run()