# coding: utf-8

import os
import tornado.web
from handlers.BaseHandler import StaticFileHandler
from handlers import Passport


urls = [
    (r"/", Passport.IndexHandler),
    (r"/login", Passport.LoginHandler),
    (r"/chat", Passport.ChatHandler),
    (r"^/(.*)$", StaticFileHandler, {"path": os.path.join(os.path.dirname(__file__), "html"), "default_filename": "index.html"}),
    tornado.web.url(r"/reverse_url", Passport.ReverseUrlHandler, {"key1": "value1", "key2": "value2"}, name="reverse_url"),
]
