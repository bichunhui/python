# coding: utf-8

import BaseHandler
import time


class IndexHandler(BaseHandler.BaseHandler):
    def get(self):
        # name = self.get_query_argument("name")
        # age = self.get_query_argument("age")
        # try:
        #     query = "insert into student(name,age) values(%(name)s,%(age)s)"
        #     self.application.db.execute(query, name=name, age=age)
        # except Exception as e:
        #     print("error occured:%s" % e)
        # else:
        #     self.write("OK")

        # self.set_cookie("key1", "value1")
        # self.set_cookie("key2", "value2", path="/new", expires=time.strptime("2018-12-18 23:59:30",
        # "%Y-%m-%d %H:%M:%S"))
        # self.set_cookie("key3", "value3", expires_days=20)
        # self.set_cookie("key4", "value4", expires=time.mktime(time.strptime("2018-12-18 23:59:30",
        # "%Y-%m-%d %H:%M:%S")))

        # count = self.get_secure_cookie("count")
        # if not count:
        #     count = 1
        #     self.set_secure_cookie("count", str(count), expires_days=1)
        # else:
        #     count = int(count)
        #     count += 1
        #     self.set_secure_cookie("count", str(count), expires_days=1)
        # self.write("count: %s" % count)

        # self.render("test2.html")
        # self.clear_all_cookies(path="/", domain=None)
        self.xsrf_token
        # self.set_cookie("key", "value", expires=time.mktime(time.strptime("2018-12-19 19:30:30", "%Y-%m-%d %H:%M:%S")))
        # self.set_cookie("key2", "value2")
        # self.write("get")
        self.render("xsrf.html")

    def post(self):
        # id = self.get_body_argument("id")
        # try:
        #     query = "select name,age from student where id=%(id)s"
        #     boy = self.application.db.get(query, id=id)
        # except Exception as e:
        #     print("error occured: %s" % e)
        # else:
        #     self.render("test1.html", boy=boy)

        # try:
        #     query = "select name,age from student where id>0"
        #     boys = self.application.db.query(query)
        # except Exception as e:
        #     print("error: %s" % e)
        # else:
        #     self.render("test1.html", boys=boys)
        self.write("post")


class LoginHandler(BaseHandler.BaseHandler):
    def get(self):
        self.write("LoginUrl")


class ReverseUrlHandler(BaseHandler.BaseHandler):
    def initialize(self, **kwargs):
        self.key1 = kwargs["key1"]
        self.key2 = kwargs["key2"]

    def get(self):
        self.write(self.key1)
        self.write(self.key2)
