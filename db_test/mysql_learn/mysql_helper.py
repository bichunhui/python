import pymysql

# db = pymysql.connect(host="localhost", port=3306, database="changshuo1", user="root", password="123")
# print(type(db))
# cursor = db.cursor()
# print(type(cursor))
# sql = "select * from students"
# cursor.execute(sql)
# data = cursor.fetchone()
# print(data)
# cursor.close()
# db.close()


class MysqlHelper():
    def __init__(self, host, port, database, user, password):
        self.__host = host
        self.__port = port
        self.__database = database
        self.__user = user
        self.__password = password

    def connect(self):
        self.__conn = pymysql.connect(host=self.__host,
                                      port=self.__port,
                                      database=self.__database,
                                      user=self.__user,
                                      password=self.__password)
        self.__cursor = self.__conn.cursor()

    def insert(self, sql, params):
        count = 0
        try:
            count = self.__cursor.execute(sql, params)
            self.__conn.commit()
            self.close()
        except Exception as e:
            print("error occur1!")
        return count

    def get_one(self, sql, params):
        result = None
        try:
            self.__cursor.execute(sql, params)
            result = self.__cursor.fetchone()
            self.close()
        except Exception as e:
            print("error occur2!")
        return result

    def get_all(self, sql, params):
        result = None
        try:
            self.__cursor.execute(sql, params)
            result = self.__cursor.fetchall()
            self.close()
        except Exception as e:
            print("error occur3!")
        return result

    def update(self, sql, params):
        count = 0
        try:
            count = self.__cursor.execute(sql, params)
            self.__conn.commit()
            self.close()
        except Exception as e:
            print("error occur4!")
        return count

    def delete(self, sql, params):
        count = 0
        try:
            count = self.__cursor.execute(sql, params)
            self.__conn.commit()
            self.close()
        except Exception as e:
            print("error occur5!")
        return count

    def close(self):
        self.__cursor.close()
        self.__conn.close()


def main():
    mysql_helper = MysqlHelper(host="localhost",
                               port=3306,
                               database="changshuo1",
                               user="root",
                               password="123")

    mysql_helper.connect()
    # sql = "insert into students(sname) values(%s)"
    # params = ("wangzilu")

    # sql = "select * from students"
    # params = None

    # sql = "select * from students"
    # params = None

    # sql = "update students set sname='haha' where sname='wangzilu'"
    # params = None

    # sql = "delete from students where sname='haha'"
    # params = None

    # mysql_helper.insert(sql, params)
    # result = mysql_helper.get_one(sql, params)
    # print(result)
    # result = mysql_helper.get_all(sql, params)
    # print(result)
    # count = mysql_helper.update(sql, params)
    # print(count)
    # count = mysql_helper.delete(sql, params)
    # print(count)


if __name__ == "__main__":
    main()

