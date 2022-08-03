"""
    api服务模块
"""

import flask  # pip install falsk
from db import RedisClient
from flask import request  # 获取地址中查询参数的功能
from flask import jsonify  # 把对象转换成字符串

# 实例化一个 app(application) 对象
# __name__   一般写法, 理解为对象的名字
app = flask.Flask(__name__)

redis_client = RedisClient()


# 视图函数, 提供服务的接口  http://demo.spiderpy.cn/get/
# @app.route('/')  将下面的视图函数挂载到路由(定义一个地址)
@app.route('/')
def index():
    # 视图函数返回数据, 只能返回字符串
    return '<h2>欢迎来到代理池</h2>'


@app.route('/get')
def get_proxy():
    """随机获取一个代理, 调用数据库的 random() 方法"""
    one_proxy = redis_client.random()
    return one_proxy


@app.route('/getnum')
def get_any_proxy():
    """获取指定数量的代理, 调用数据库的 count_for_num() 方法"""
    # 怎么取查询参数
    num = request.args.get('num', '')  # -- 字符串
    # 有可能用户没有输入查询参数
    if not num:  # 如果没有获取到查询参数
        num = 1
    else:
        num = int(num)

    any_proxy = redis_client.count_for_num(num)
    return jsonify(any_proxy)


@app.route('/getcount')
def get_count_proxy():
    """获取所有代理的数量, 调用数据库的 count() 方法"""
    count_proxies = redis_client.count()

    return f'代理池还有 {count_proxies} 代理可用!!!!'

@app.route('/getall')
def get_all_proxy():
    """获取所有代理, 调用数据库的 all() 方法"""
    all_proxy = redis_client.all()
    return jsonify(all_proxy)


if __name__ == '__main__':
    # 运行实例化的 app 对象
    app.run()
