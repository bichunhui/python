from mysql_helper import MysqlHelper
from hashlib import sha1


def register(uname, password):
    mysql_helper = MysqlHelper(host="localhost",
                               port=3306,
                               database="changshuo1",
                               user="root",
                               password="123")

    mysql_helper.connect()
    s1 = sha1()
    s1.update(password.encode("utf-8"))
    s1_password = s1.hexdigest()
    sql = "insert into userinfos values(0, %s, %s, 0)"
    params = (uname, s1_password)
    count = mysql_helper.insert(sql, params)
    if count != 0:
        print("注册成功")
    else:
        print("注册失败")


def land(uname, password):
    mysql_helper = MysqlHelper(host="localhost",
                               port=3306,
                               database="changshuo1",
                               user="root",
                               password="123")

    mysql_helper.connect()
    s1 = sha1()
    s1.update(password.encode("utf-8"))
    s1_password = s1.hexdigest()
    # print(s1_password)
    sql = "select upwd from userinfos where uname=%s"
    params = (uname,)
    upwd = mysql_helper.get_one(sql, params)[0]
    # print(upwd)
    if upwd == s1_password:
        print("密码正确")
    else:
        print("密码错误")


def main():
    register("bichunhui", "122466")
    # land("bichunhui", "122466")


if __name__ == "__main__":
    main()
