import redis

# 建立redis数据库的连接对象
r = redis.Redis(host='127.0.0.1',  # 表示本地的redis数据库
            port=6379,
            db=0,
            decode_responses=True  # 当设置为True以后, 那么Redis数据库就不使用二进制存储数据
            )

print(r)

print(r.smembers('myset'))
print(r.hgetall('user:1000'))


r.set('name', '张三')
print(r.get('name'))


# mapping 映射关系, 一般指字典的键值对
r.mset({'age': 18, 'hobby': '吃喝玩乐'})

print(r.mget('name', 'age', 'hobby'))  # 返回的是一个列表

