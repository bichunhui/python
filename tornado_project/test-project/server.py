# coding:utf-8

import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options
import config
import urls
import torndb
import redis


tornado.options.define("port", default=8000, type=int, help="port_setting")


class Application(tornado.web.Application):
    def __init__(self, *args, **kwargs):
        super(Application, self).__init__(*args, **kwargs)
        self.db = torndb.Connection(**config.mysql_options)
        self.redis = redis.StrictRedis(**config.redis_options)


def main():
    tornado.options.options.parse_command_line()
    app = Application(urls.urls, **config.settings)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.bind(tornado.options.options.port)
    # print(tornado.options.options.port)
    http_server.start()
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
