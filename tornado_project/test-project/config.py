# coding:utf-8
import os

settings = dict(
    static_path = os.path.join(os.path.dirname(__file__), "static"),
    template_path = os.path.join(os.path.dirname(__file__), "html"),
    cookie_secret = "VnQKxbi+R1iU2MRLIPihTZMc/23fMkANoBQYqwMxMkI=",
    xsrf_cookies = True,
    login_url = "/login",
    debug = True
)

mysql_options = dict(
    host = "127.0.0.1",
    database = "ihome",
    user = "root",
    password = "123"
)

redis_options = dict(
    host = "127.0.0.1",
    port = "6379"
)
