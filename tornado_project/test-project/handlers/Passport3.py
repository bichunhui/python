# coding: utf-8

import BaseHandler
import tornado.web


class IndexHandler(BaseHandler.BaseHandler):
    def get_current_user(self):
        if not self.get_query_argument("f", ""):
            return False
        else:
            return True

    @tornado.web.authenticated
    def get(self):
        self.write("get")

    def post(self):
        self.write("post")


class LoginHandler(BaseHandler.BaseHandler):
    def get(self):
        next_url = self.get_query_argument("next", "")
        if next_url:
            self.write("转来手动登录后")
            self.redirect(next_url+"?f=login")
        else:
            self.write("请手动登录")
            self.redirect("/?f=login")


class ReverseUrlHandler(BaseHandler.BaseHandler):
    def initialize(self, **kwargs):
        self.key1 = kwargs["key1"]
        self.key2 = kwargs["key2"]

    def get(self):
        self.write(self.key1)
        self.write(self.key2)