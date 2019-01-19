# coding: utf-8

import BaseHandler
from tornado.websocket import WebSocketHandler


class IndexHandler(BaseHandler.BaseHandler):
    def get(self):
        self.render("chat.html")

    def post(self):
        self.write("post")


class ChatHandler(WebSocketHandler):

    users = []

    def open(self):
        for user in self.users:
            user.write_message("%s上线了" % self.request.remote_ip)
        self.users.append(self)

    def on_message(self, msg):
        for user in self.users:
            user.write_message(u"%s说:%s" % (self.request.remote_ip, msg))

    def on_close(self):
        self.users.remove(self)
        for user in self.users:
            user.write_message("%s下线了" % self.request.remote_ip)

    def check_origin(self, origin):
        return True    # 允许websocket跨域请求


class LoginHandler(BaseHandler.BaseHandler):
    def get(self):
        self.write("LoginHandler")


class ReverseUrlHandler(BaseHandler.BaseHandler):
    def initialize(self, **kwargs):
        self.key1 = kwargs["key1"]
        self.key2 = kwargs["key2"]

    def get(self):
        self.write(self.key1)
        self.write(self.key2)
