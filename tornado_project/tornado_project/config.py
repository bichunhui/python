# coding: utf-8

import os

settings = dict(
    static_path = os.path.join(os.path.dirname(__file__), "static"),
    template_path = os.path.join(os.path.dirname(__file__), "html"),
    login_url = "/login",
    cookie_secret = "MCnlDYRZR0iQ600OOSAgecs5vlmxOUJftlvdMimXgnU=",
    xsrf_cookies = True,
    debug = True
)

mysql_options = dict(
    host = "127.0.0.1",
    user = "root",
    database = "ihome",
    password = "123"

)

redis_options = dict(
    host = "127.0.0.1",
    port = 6379
)

log_file = os.path.join(os.path.dirname(__file__), "logs/log")
log_level = "debug"

# 密码加密密钥
passwd_hash_key = "nlgCjaTXQX2jpupQFQLoQo5N4OkEmkeHsHD9+BBx2WQ="
