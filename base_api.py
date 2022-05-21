# -*- coding:utf-8 -*-
# 作者：IT小学生蔡坨坨（caituotuo.top）
# 时间：2021/10/08 23:31
# 功能：对接口测试框架Requests进行二次封装，完成对api的驱动

import requests
import traceback

from utils.get_logger import GetLogger
from utils.get_time import GetTime
from utils.get_yml_data import GetYmlData


class BaseApi:
    def __init__(self):
        self.logger = GetLogger().get_logger()
        self.now_datetime = GetTime().get_now_datetime()
        self.config = GetYmlData().get_config()

    def requests_http(self, req):
        """
        使用Python关键字传参的方式，将请求结构体传给requests.request()方法
        :param req: 请求数据，字典格式，包括url、method、headers、param、data、json、files等
        :return: result
        """

        # 传统的写法：
        # r = requests.request(method="post",
        #                      url="http://ip:port/login",
        #                      params={"username": "sang", "password": "123"})

        try:
            # ** 解包，将字典格式解包成 method="post",url="http://ip:port/login"
            result = requests.request(**req, timeout=10)
            return result
        except Exception as e:
            self.logger.error("接口请求失败！")
            self.logger.error(traceback.format_exc())
            self.logger.error(e)
