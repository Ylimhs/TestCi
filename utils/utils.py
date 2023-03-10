# -*- coding: UTF-8 -*-
import datetime
import json
import logging
import os

import requests
print("当前路径 -  %s" %os.getcwd())
# 配置日志显示
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='log/task.log',
                    filemode='a',
                    encoding='utf-8')


class LarkException(Exception):
    def __init__(self, code=0, msg=None):
        self.code = code
        self.msg = msg

    def __str__(self) -> str:
        return "{}:{}".format(self.code, self.msg)

    __repr__ = __str__


def request(method, url, headers, payload={}):
    response = requests.request(method, url, headers=headers, json=payload)
    logging.info("URL: " + url)
    # logging.info("headers:\n" + json.dumps(headers, indent=2, ensure_ascii=False))
    logging.info("payload: " + json.dumps(payload, indent=2, ensure_ascii=False))
    if response.status_code >= 400:
        response.raise_for_status()
    return response


def is_past_date(date_str):
    """判断给定日期是否小于当前日期和时间"""
    try:
        given_date = datetime.datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
        current_date = datetime.datetime.now()
        return given_date < current_date
    except Exception as e:
        pass
    return True


def strToTime(timeStr):
    """格式化当前日期和时间"""
    try:
        return datetime.datetime.strptime(timeStr, '%Y-%m-%d %H:%M:%S')
    except Exception as e:
        pass
    return None
