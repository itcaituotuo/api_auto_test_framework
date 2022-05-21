# -*- coding:utf-8 -*-
# 作者：蔡合升
# 时间：2022/5/16 16:39
# 功能：时间封装

import time
import traceback

from utils.get_logger import GetLogger


class GetTime:
    def __init__(self):
        self.logger = GetLogger().get_logger()

    def get_now_datetime(self):
        try:
            now_datetime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
            return now_datetime
        except Exception as e:
            self.logger.error(traceback.format_exc())
            self.logger.error("获取时间失败：" + str(e))


if __name__ == '__main__':
    print(GetTime().get_now_datetime())
