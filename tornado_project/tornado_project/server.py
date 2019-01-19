# coding: utf-8

import tornado.options
import tornado.web
import tornado.httpserver
import tornado.ioloop
import torndb
import redis
import config
import urls


tornado.options.define("port", default=8000, type=int, help="port define")


class Application(tornado.web.Application):
    def __init__(self, *args, **kwargs):
        super(Application, self).__init__(*args, **kwargs)
        self.db = torndb.Connection(**config.mysql_options)
        self.redis = redis.StrictRedis(**config.redis_options)


def main():
    # tornado.options.options.log_file_prefix = config.log_file
    # tornado.options.options.logging = config.log_level
    tornado.options.options.parse_command_line()

    app = Application(urls.url, **config.settings)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.bind(tornado.options.options.port)
    http_server.start()
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
