import redis


class RedisHelper(object):
    def __init__(self):
        pool = redis.ConnectionPool(host='192.168.16.59', port=6379)
        conn = redis.Redis(connection_pool=pool)
        self.conn = conn

    def set(self, name, k, v):
        self.conn.set(name, k, v)

    def delete(self, name, k):
        self.conn.hdel('foo', 'Bar')


conn = RedisHelper().conn