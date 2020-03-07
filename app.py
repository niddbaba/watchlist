from flask import Flask, escape, url_for
'''
由模块名字默认程序名字
'''
app = Flask(__name__)


@app.route('/')
def hello():
    return '<h1>Welcome to my personal website!</h1>'


@app.route('/user/<name>')
def user_page(name):
    # 解析html文件显示在网站上
    return "user :%s" % escape(name)


@app.route('/test')
def test_url_for():
    # url_for参数为函数名字，用于打印执行该函数的地址

    print(url_for('hello'))
    print(url_for('user_page', name='weige'))
    print(url_for('test_url_for'))
    print(url_for('test_url_for', num=2))
    return 'Test Page'
