# coding=gbk

# coding=utf-8

# -*- coding: UTF-8 -*-

from CCPRestSDK import REST
import ConfigParser

# ���ʺ�
accountSid = "8aaf070867aa74db0167e13fcc890103"  # '�������ʺ�'

# ���ʺ�Token
accountToken = "37c9011b2a914e1d9532512e93e2fb7a"  # '�������ʺ�Token'

# Ӧ��Id
appId = "8aaf070867aa74db0167e13fccab0104"  # '����Ӧ��ID'

# �����ַ����ʽ���£�����Ҫдhttp://
serverIP = 'app.cloopen.com'

# ����˿�
serverPort = '8883'

# REST�汾��
softVersion = '2013-12-26'


# ����ģ�����
# @param to �ֻ�����
# @param datas �������� ��ʽΪ���� ���磺{'12','34'}���粻���滻���� ''
# @param $tempId ģ��Id

# def sendTemplateSMS(to, datas, tempId):
#     # ��ʼ��REST SDK
#     rest = REST(serverIP, serverPort, softVersion)
#     rest.setAccount(accountSid, accountToken)
#     rest.setAppId(appId)
#
#     result = rest.sendTemplateSMS(to, datas, tempId)
#     for k, v in result.iteritems():
#
#         if k == 'templateSMS':
#             for k, s in v.iteritems():
#                 print '%s:%s' % (k, s)
#         else:
#             print '%s:%s' % (k, v)
class _CCP(object):
    def __init__(self):
        self.rest = REST(serverIP, serverPort, softVersion)
        self.rest.setAccount(accountSid, accountToken)
        self.rest.setAppId(appId)

    @classmethod
    def instance(cls):
        if not hasattr(cls, "_instance"):
            cls._instance = cls()
        return cls._instance

    def sendTemplateSMS(self, to, datas, tempId):
        return self.rest.sendTemplateSMS(to, datas, tempId)


ccp = _CCP.instance()

if __name__ == "__main__":
    ccp.sendTemplateSMS("15353702776", ["1234", 5], 1)
# sendTemplateSMS(�ֻ�����,��������,ģ��Id)