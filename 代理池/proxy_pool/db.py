"""
数据库存储模块
"""
import redis
import random
from config import REDIS_HOST, REDIS_PORT, REDIS_DATABASE, REDIS_OBJECT
from config import INIT_SCORE, HIGH_SCORE, MINIMUM_SCORE, HIGHEST_SCORE
from config import CHANGE_SCORE


class RedisClient:
    """数据库类"""

    def __init__(self, host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DATABASE):
        """初始化数据库, 连接数据库"""
        self.db = redis.Redis(host=host, port=port, db=db, decode_responses=True)

    def exists(self, proxy):
        """判断传入的代理, 是否在已经勋在数据库"""
        # 有代理在数据库中 返回True
        # 没有代理在数据库中 返回False
        return not self.db.zscore(REDIS_OBJECT, proxy) is None

    def add(self, proxy, score=INIT_SCORE):
        """
        添加代理到数据库, 设置初始评分
        :param proxy: 传入的代理
        :param score: 设置的初始分数
        """
        if not self.exists(proxy):  # 如果数据库中没有当前传进来的代理数据
            # 数据插入
            return self.db.zadd(REDIS_OBJECT, {proxy: score})

    def random(self):
        """随机选择一个代理"""
        # 1. 尝试获取满分100的代理,
        proxies = self.db.zrangebyscore(REDIS_OBJECT, HIGH_SCORE, HIGH_SCORE)
        if len(proxies):  # 非0即真
            return random.choice(proxies)
        # 2. 尝试获取最低分到最高分中间范围代理的数据
        proxies = self.db.zrangebyscore(REDIS_OBJECT, MINIMUM_SCORE, HIGHEST_SCORE)
        if len(proxies):
            return random.choice(proxies)
        # 3. 如果查询不到数据, 那么久提示没有数据
        print('########---数据为空---########')

    def decrease(self, proxy):
        """传入一个代理, 如果检测不过关, 那么评分执行减分的操作"""
        self.db.zincrby(REDIS_OBJECT, CHANGE_SCORE, proxy)  # 把传入的代理减分
        score = self.db.zscore(REDIS_OBJECT, proxy)  # 查询代理分数
        if score <= 0:
            self.db.zrem(REDIS_OBJECT, proxy)


    def max(self, proxy):
        """传入一个代理, 如果检测过关, 讲代理设置为100"""
        return self.db.zadd(REDIS_OBJECT, {proxy: HIGH_SCORE})

    def count(self):
        """获取数据库中所有代理的数量"""
        return self.db.zcard(REDIS_OBJECT)

    def all(self):
        """获取所有代理, 返回的列表"""
        proxies = self.db.zrangebyscore(REDIS_OBJECT, 1, 100)
        if proxies:
            return proxies
        else:
            print('########---数据为空---########')

    def count_for_num(self, number):
        """指定数量获取代理, 返回一个列表"""
        all_proxies = self.all()
        # random.sample 随机在对象中取不同的数据
        proxies = random.sample(all_proxies, k=number)
        return proxies



if __name__ == '__main__':
    # 实例化数据库对象
    redis_client = RedisClient()

    proxies = ['927.72.91.211:9999', '927.12.91.211:8888', '927.792.91.219:7777', '927.732.91.211:6666']

    # for pro in proxies:
    #     redis_client.add(pro)

    # result = redis_client.random()
    # print(result)

    # redis_client.decrease('927.72.91.211:9999')

    # redis_client.max('927.12.91.211:8888')

    count = redis_client.count_for_num(3)
    print(count)


