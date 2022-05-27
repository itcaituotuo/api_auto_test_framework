# -*- coding:utf-8 -*-
# 作者：IT小学生蔡坨坨（caituotuo.top）
# 时间：2022/5/21 20:20
# 功能：将http请求封装成Python方法

from base_api import BaseApi
from utils.get_yml_data import GetYmlData


class DaXue(BaseApi):
    def __init__(self):
        super(DaXue, self).__init__()

    # 接口信息
    # Request URL
    url = "/home/daxue/ajax"
    # Request Method
    method = "POST"
    # ContentType
    content_type = "application/x-www-form-urlencoded"

    # def daxue(self, data_path):
    #     data = GetYmlData().get_yml_data(data_path)
    #     req = {
    #         "url": self.config["url"] + self.url,
    #         "method": self.method,
    #         "headers": self.config["headers"],
    #         "data": data["req"]
    #     }
    #     res = self.requests_http(req)
    #     assert res.status_code == 200
    #     res_json = res.json()
    #     self.logger.info(res_json)
    #     assert res_json["status"] == data["res"]["status"]

    def daxue(self, data_path):
        data = GetYmlData().get_yml_data(data_path)
        res = self.api_temp(self.url, self.method, self.content_type, data)
        return res


if __name__ == '__main__':
    DaXue().daxue("data/req.yml")
