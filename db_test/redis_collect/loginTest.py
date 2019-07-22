from mysql_learn.mysql_helper import MysqlHelper
from redis_collect.redis_helper import RedisHelper
from hashlib import sha1


def login(uname, password):
    # 首先查看redis数据库中是否有uname所对应的password
    # redis中没有的话就查询mysql数据库，并保存在redis数据库中
    # 下次直接从redis数据库中取出
    redishelper = RedisHelper(host="localhost", port=6379)
    redishelper.connect()
    pwd = redishelper.get(uname)
    if pwd:
        # 比较两个密码
        if pwd == password:
            return True
    else:
        # 从mysql中取出并存到redis中
        mysqlhelper = MysqlHelper(host="localhost", port=3306, database="changshuo1", user="root", password="123")
        mysqlhelper.connect()
        sql = "select upwd from userinfos where uname=%s"
        params = uname
        pwd = mysqlhelper.get_one(sql, params)[0]
        print(pwd)
        if pwd:
            if pwd == password:
                return True
            redishelper.set(uname, pwd)
        else:
            return False


def my_sha1(password):
    s1 = sha1()
    s1.update(password.encode("utf-8"))
    return s1.hexdigest()


def main():
    uname = "bichunhui"
    password = "122466"
    password = my_sha1(password)
    flag = login(uname, password)
    if flag:
        print("登录成功！")
    else:
        print("登陆失败！")


if __name__ == "__main__":
    main()