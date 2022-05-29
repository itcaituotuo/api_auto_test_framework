# -*- coding:utf-8 -*-
# 作者：IT小学生蔡坨坨（caituotuo.top）
# 时间：2021/10/08 23:31
# 功能：对接口测试框架Requests进行二次封装，完成对api的驱动

import requests
import traceback
import jsonpath

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
        #                      json={"username": "sang", "password": "123"})

        try:
            # ** 解包，将字典格式数据解包成 method="post",url="http://ip:port/login",……
            result = requests.request(**req, timeout=10)
            return result
        except Exception as e:
            self.logger.error("接口请求失败！")
            self.logger.error(traceback.format_exc())
            self.logger.error(e)

    def api_temp(self, request_url, method, content_type, data) -> dict:
        """
        接口请求封装
        :param request_url: Request URL
        :param method: Request Method
        :param content_type: ContentType
        :param data: 请求参数
        :return:
        """

        # 判断请求数据格式 data/json/params
        data_type = ""
        method = method.upper()
        if method == "POST":
            if content_type == "application/x-www-form-urlencoded":
                data_type = "data"
            elif content_type == "application/json":
                data_type = "json"
        elif method == "GET":
            data_type = "params"
        else:
            self.logger.error("method或content_type有误！")
        req = {
            "url": self.config["url"] + request_url,
            "method": method,
            "headers": self.config["headers"],
            data_type: data["req"]
        }
        self.logger.info("请求数据：" + str(req))
        res = self.requests_http(req)
        assert res.status_code == 200
        res_json = res.json()
        self.logger.debug("响应数据：" + str(res_json))
        for key in data["res"]:
            """ 断言结果 """
            actual = jsonpath.jsonpath(res_json, "$..{}".format(key))[0]  # 默认第一个
            expect = data["res"][key]
            self.logger.info("实际结果：{}={}，预期结果：{}={}".format(key, actual, key, expect))
            assert actual == expect
        return res_json
