from redis import StrictRedis, ConnectionPool

# pool = ConnectionPool(host="localhost", port=6379, db=0, password=None)
# redis = StrictRedis(connection_pool=pool)
# 上下两种redis创建方式是一样的
# redis = StrictRedis(host="localhost", port=6379, db=0, password=None)
# count = redis.delete("age", "age1")
# print(count)

# redis.set("gender", 1)
# redis.set("name", "fanjiahui")
# redis.delete("age")
# print(redis.get("gender"))


class RedisHelper():
    def __init__(self, host, port, db=None, password=None):
        self.__host = host
        self.__port = port
        self.__db = db
        self.__password = password

    def connect(self):
        try:
            self.__pool = ConnectionPool(host=self.__host,
                                         port=self.__port,
                                         db=self.__db,
                                         password=self.__password)
            self.__redis = StrictRedis(connection_pool=self.__pool)
            # print("连接成功")
        except Exception as e:
            print("redis连接失败")

    def set(self, key, value):
        try:
            temp = self.__redis.set(key, value)
            return temp
        except Exception as e:
            print("redis set error occur!")

    def get(self, key):
        try:
            temp = self.__redis.get(key)
            return temp
        except Exception as e:
            print("redis get error occur!")
            return None

    def delete(self, *args):
        count = self.__redis.delete(*args)
        return count


def main():
    redis_helper = RedisHelper(host="localhost", port=6379, db=None, password=None)
    redis_helper.connect()
    # count = redis_helper.set("name", "fanjiale")
    # print(count)
    # value = redis_helper.get("name")
    # print(value)
    num = redis_helper.delete("name")
    print(num)


if __name__ == "__main__":
    main()



