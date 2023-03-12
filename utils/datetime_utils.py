# -*- coding:utf-8 -*-
# 作者：测试蔡坨坨
# 时间：2022/5/16 16:39
# 功能：时间封装

import time
import traceback

from utils.log_utils import LogUtils


class DateTimeUtils:
    def __init__(self):
        self.logger = LogUtils().get_logger()

    def get_now_datetime(self):
        try:
            now_datetime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
            return now_datetime
        except Exception as e:
            self.logger.error(traceback.format_exc())
            self.logger.error("获取时间失败：" + str(e))


if __name__ == '__main__':
    print(DateTimeUtils().get_now_datetime())
