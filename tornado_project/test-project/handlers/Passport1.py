# coding: utf-8

import BaseHandler


class IndexHandler(BaseHandler.BaseHandler):
    def get(self):
        # reverse_url = self.reverse_url("reverse_url")
        # self.write("<a href=%s><h1>reverse_url</h1></a>" % reverse_url)
        #
        # query_arg = self.get_query_argument("a", strip=False)
        # query_args = self.get_query_arguments("a")
        #
        # rep = "query_arg: %s<br/>" % query_arg
        # rep += "query_args: %s<br/>" % query_args
        #
        # self.write(rep)
        # print(type(query_args))   # list
        # print(query_arg)    # 带空格的参数
        #
        # dict = {"key1": "value1", "key2": "value2", "key3": "value3"}
        # self.write(dict)    # 以下为手动转换
        #
        # dict = {"key3": "value3", "key4": "value4"}
        # dict_json = json.dumps(dict)
        # # self.set_header("Content-Type", "application/json, charset=UTF-8")
        #
        # # self.set_status(211, "211error")
        # # self.set_status(404)
        #
        # self.write(dict_json)
        #
        # self.redirect("/login")

        self.write("OK")   # redirect后后面不能再输出了

        # house_info = {
        #     "p1": 198,
        #     "p2": 200,
        #     "title": ["宽窄巷子", "160平大空间", "文化保护区双地铁"],
        #     "score": 5,
        #     "comments": 6,
        #     "position": "北京市丰台区六里桥地铁"
        # }
        # self.render("index.html", **house_info)

        # self.render("new.html", text="")

        def func(a):
            return a
        a = "<script>alert('fanjiale')</script>"
        self.render("test1.html", func=func, a=a)

    def post(self):
        # body_arg = self.get_body_argument("b")
        # body_args = self.get_body_arguments("b",)
        # arg = self.get_argument("c")
        # args = self.get_arguments("c")
        #
        # try:
        #     missing_arg = self.get_argument("d")
        # except Exception as e:
        #     print(e)
        #
        # rep = "body_arg: %s<br/>" % body_arg
        # rep += "body_args: %s<br/>" % body_args
        # rep += "arg: %s<br/>" % arg
        # rep += "args: %s<br/>" % args
        #
        # self.write(rep)
        #
        # files = self.request.files
        # img_files = files.get("img")
        # if img_files:
        #     img_file = img_files[0]["body"]
        #     file = open("./img.jpg", "w+")
        #     file.write(img_file)
        #     file.close()
        #
        # self.write(self.json_dict)

        # self.send_error(211, content="出现211错误!")

        # print(self.request.headers["Cookie"])

        self.write("OK")  # send_error 后面不能输出了

        # text = self.get_argument("text", "")
        # self.render("new.html", text=text)


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
