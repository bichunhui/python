# coding: utf-8

import BaseHandler
import logging
import re
import hashlib
import config

from utils.response_code import RET
from utils.session import Session
from utils.commons import required_login


class IndexHandler(BaseHandler.BaseHandler):
    def get(self):
        # logging.debug("debug msg")
        # logging.info("info msg")
        # logging.warning("warning msg")
        # logging.error("error msg")    # tail -f log
        # print("print msg")
        # self.write("get")
        self.render("index.html")

    def post(self):
        self.write("post")


class RegisterHandler(BaseHandler.BaseHandler):
    """注册"""
    def post(self):
        # 获取参数
        mobile = self.json_args.get("mobile")
        phonecode = self.json_args.get("phonecode")
        password = self.json_args.get("password")

        # 检查参数
        if not all((mobile, phonecode, password)):
            return self.write(dict(errcode=RET.PARAMERR, errmsg="参数不完整"))

        if not re.match(r"^1\d{10}$", mobile):
            return self.write(dict(errcode=RET.DATAERR, errmsg="手机号格式错误"))

        # 如果产品对于密码长度有限制，需要在此作出判断
        # if len(password)<6
        # 判断短信验证码是否正确

        try:
            real_sms_code = self.redis.get("smscode_%s" % mobile)
        except Exception as e:
            logging.error(e)
            return self.write(dict(errcode=RET.DBERR, errmsg="查询验证码出错"))

        # 判断短信验证码是否过期
        if not real_sms_code:
            return self.write(dict(errcode=RET.NODATA, errmsg="验证码过期"))

        # 对比用户填写的验证码于真实值
        if real_sms_code != phonecode:
            return self.write(dict(errcode=RET.DATAERR, errmsg="验证码错误"))

        try:
            self.redis.delete("smscode_%s" % mobile)
        except Exception as e:
            logging.error(e)

        # 保存数据，同时判断手机号是否存在，判断的依据是数据库中的mobile字段的唯一约束
        passwd = hashlib.sha256(password + config.passwd_hash_key).hexdigest()
        print(mobile, passwd)
        sql = "insert into ih_user_profile(up_name,up_mobile,up_passwd,up_admin) values(%(name)s,%(mobile)s,%(passwd)s,%(admin)s);"
        try:
            user_id = self.db.execute(sql, name=mobile, mobile=mobile, passwd=passwd, admin="0")
        except Exception as e:
            logging.error(e)
            print(e)
            return self.write(dict(errcode=RET.DATAEXIST, errmsg="手机号已存在"))

        # 用session记录用户的登录状态
        session = Session(self)
        session.data["user_id"] = user_id
        session.data["mobile"] = mobile
        session.data["name"] = mobile
        try:
            session.save()
        except Exception as e:
            logging.error(e)
        self.write(dict(errcode=RET.OK, errmsg="注册成功"))


class LoginHandler(BaseHandler.BaseHandler):
    # def get(self):
        # self.write("LoginHandler")
        # self.xsrf_token
        # self.render("login.html")

    def post(self):
        # print("haha")
        # self.write({"a": "haha"})
        mobile = self.json_args.get("mobile")
        password = self.json_args.get("password")

        # 检查参数
        if not all((mobile, password)):
            return self.write(dict(errcode=RET.PARAMERR, errmsg="参数错误"))
        if not re.match(r"^1\d{10}$", mobile):
            return self.write(dict(errcode=RET.DATAERR, errmsg="手机号错误"))

        # 检查密码是否正确
        res = self.db.get("select up_user_id,up_name,up_passwd from ih_user_profile where up_mobile=%(mobile)s;", mobile=mobile)
        password = hashlib.sha256(password + config.passwd_hash_key).hexdigest()
        if res and res["up_passwd"] == unicode(password):
            # 生成session数据
            # 返回客户端
            try:
                self.session = Session(self)
                self.session.data["user_id"] = res["up_user_id"]
                self.session.data["name"] = res["up_name"]
                self.session.data["mobile"] = mobile
            except Exception as e:
                logging.error(e)
            return self.write(dict(errcode=RET.OK, errmsg="OK"))
        else:
            self.write(dict(errcode=RET.DATAERR, errmsg="手机号或密码错误"))


class LogoutHandler(BaseHandler.BaseHandler):
    """退出登录"""
    @required_login
    def get(self):
        # 清除session数据
        # session = Session(self)
        self.session.clear()
        self.write(dict(errcode=RET.OK, errmsg="退出成功"))


class CheckLoginHandler(BaseHandler.BaseHandler):
    """检查登录状态"""
    pass


class ReverseUrlHandler(BaseHandler.BaseHandler):
    def initialize(self, *args, **kwargs):
        self.key1 = kwargs["key1"]
        self.key2 = kwargs["key2"]

    def get(self):
        self.write(self.key1)
        self.write(self.key2)
