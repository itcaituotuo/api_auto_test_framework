# -*- coding:utf-8 -*-
# 作者：IT小学生蔡坨坨（caituotuo.top）
# 时间：2022/5/21 21:46
# 功能：Python自动化线性脚本

import requests

res = requests.post(url="https://www.iamwawa.cn/home/daxue/ajax",
                    headers={"user-agent": "Chrome"},
                    data={"type": "name", "keyword": "四川轻化工大学"})
assert res.status_code == 200
res_json = res.json()
print(res_json)
assert res_json["status"] == 1
