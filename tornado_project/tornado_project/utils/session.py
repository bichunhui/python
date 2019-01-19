# coding: utf-8

import uuid
import logging
import json
import constants


class Session(object):
    """"""
    def __init__(self, request_handler_obj):
        # 先判断用户是否已经有了session_id
        self.request_handler = request_handler_obj
        self.session_id = request_handler_obj.get_secure_cookie("session_id")

        # 如果不存在session_id,生成session_id
        if not self.session_id:
            self.session_id = uuid.uuid4().hex
            self.data = {}
            request_handler_obj.set_secure_cookie("session_id", self.session_id)

        # 如果存在session_id,去redis中取出data
        else:
            global json_data
            try:
                json_data = request_handler_obj.redis.get("sess_%s" % self.session_id)
            except Exception as e:
                logging.error(e)
                self.data = {}
            if not json_data:
                self.data = {}
            else:
                self.data = json.loads(json_data)

    def save(self):
        json_data = json.dumps(self.data)
        try:
            self.request_handler.redis.setex("sess_%s" % self.session_id, constants.SESSION_EXPIRES_SECONDS, json_data)
        except Exception as e:
            logging.error(e)
            raise Exception("save session failed")

    def clear(self):
        try:
            self.request_handler.redis.delete("sess_%s" % self.session_id)
        except Exception as e:
            logging.error(e)
        self.request_handler.clear_cookie("session_id")














