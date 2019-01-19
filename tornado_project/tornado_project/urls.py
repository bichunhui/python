# coding: utf-8

from handlers import Passport
from handlers import BaseHandler
from handlers import VerifyCode
from tornado.web import url
import os

url = [
    # (r"/", Passport.IndexHandler),
    (r"/api/login", Passport.LoginHandler),
    (r"/api/imagecode", VerifyCode.ImageCodeHandler),
    (r"/api/smscode", VerifyCode.SMSCodeHandler),
    (r"/api/register", Passport.RegisterHandler),
    url(r"/reverse_url", Passport.ReverseUrlHandler, {"key1": "value1", "key2": "value2"}, name="reverse_url"),
    (r"/(.*)", BaseHandler.StaticFileHandler, {"path": os.path.join(os.path.dirname(__file__), "html"), "default_filename": "index.html"}),

]