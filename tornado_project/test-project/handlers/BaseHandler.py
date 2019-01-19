import tornado.web
import json


class BaseHandler(tornado.web.RequestHandler):
    # def set_default_headers(self):
    #     self.set_header("Content-Type", "application/json, charset=UTF-8")

    def prepare(self):
        if self.request.headers.get("Content-Type"):
            if self.request.headers.get("Content-Type").startswith("application/json"):
                self.json_dict = json.loads(self.request.body)
            else:
                self.json_dict = None

    def initialize(self):
        pass

    def write_error(self, status_code, **kwargs):
        # self.write("status_code: %d<br/>contents: %s" % (status_code, kwargs["content"]))
        pass

    def on_finish(self):
        pass


class StaticFileHandler(tornado.web.StaticFileHandler):
    def __init__(self, *args, **kwargs):
        # tornado.web.StaticFileHandler.__init__(self, *args, **kwargs)
        super(StaticFileHandler, self).__init__(*args, **kwargs)
        self.xsrf_token
