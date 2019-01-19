# coding:utf-8

import constants
import logging
import re
import random

from BaseHandler import BaseHandler
from utils.response_code import RET
from utils.captcha.captcha import captcha
from libs.yuntongxun.CCP import ccp


class ImageCodeHandler(BaseHandler):
    """图片验证码"""
    def get(self):
        """获取图片验证码"""
        pre_image_id = self.get_argument("pre_image_id", "")
        cur_image_id = self.get_argument("cur_image_id", "")
        # if not cur_image_id:
        #     return self.write(dict(errcode=RET.NODATA, errmsg="缺少图片验证码id"))
        name, text, pic = captcha.generate_captcha()
        try:
            if pre_image_id:
                self.redis.delete("image_code_%s" % pre_image_id)
            self.redis.setex("image_code_%s" % cur_image_id, constants.IMAGE_CODE_EXPIRES_SECONDS, text)
        except Exception as e:
            logging.error(e)
            self.write("")
        else:
            self.set_header("Content-Type", "image/jpg")
            self.write(pic)


class SMSCodeHandler(BaseHandler):
    """短信验证码"""
    def post(self):
        # 获取参数
        mobile = self.json_args.get("mobile")
        imagecode = self.json_args.get("imagecode")
        imagecodeid = self.json_args.get("imagecodeid")
        # 校验参数
        if not all((mobile, imagecode, imagecodeid)):
            return self.write(dict(errcode=RET.PARAMERR, errmsg="参数缺失"))
        if not re.match(r"^1\d{10}$", mobile):
            return self.write(dict(errcode=RET.PARAMERR, errmsg="手机号格式错误"))

        # 获取图片验证码真实值
        try:
            real_imagecode = self.redis.get("image_code_%s" % imagecodeid)
        except Exception as e:
            logging.error(e)
            return self.write(dict(errcode=RET.DBERR, errmsg="查询验证码出错"))
        if not real_imagecode:
            return self.write(dict(errcode=RET.NODATA, errmsg="验证码过期"))
        if real_imagecode.lower() != imagecode.lower():
            return self.write(dict(errcode=RET.DATAERR, errmsg="验证码错误"))

        # 删除图片验证码
        try:
            self.redis.delete("image_code_%s" % imagecodeid)
        except Exception as e:
            logging.error(e)

        # 手机号是否存在检查
        sql = "select count(*) counts from ih_user_profile where up_mobile=%s"
        try:
            ret = self.db.get(sql, mobile)
        except Exception as e:
            logging.error(e)
            return self.write(dict(errcode=RET.DBERR, errmsg="查询手机号错误"))
        else:
            if 0 != ret.counts:
                return self.write(dict(errcode=RET.DATAERR, errmsg="手机号已注册"))

        # 产生随机短信验证码
        smscode = "%04d" % random.randint(1, 9999)
        try:
            self.redis.setex("smscode_%s" % mobile, constants.SMS_CODE_EXPIRES_SECONDS, smscode)
        except Exception as e:
            logging.error(e)
            return self.write(dict(errcode=RET.DBERR, errmsg="数据库出错"))

        # 发送短信验证码
        try:
            result = ccp.sendTemplateSMS(mobile, [smscode, constants.SMS_CODE_EXPIRES_SECONDS/60], 1)
        except Exception as e:
            logging.error(e)
            return self.write(dict(errcode=RET.THIRDERR, errmsg="发送短信失败"))
        if result:
            self.write(dict(errcode=RET.OK, errmsg="发送成功"))
        else:
            self.write(dict(errcode=RET.UNKOWNERR, errmsg="发送失败"))
        # self.write(dict(errcode=RET.OK, errmsg="ok"))
        print("smscode_%s=%s" % (mobile, smscode))
