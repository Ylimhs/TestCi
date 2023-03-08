# -*- coding: UTF-8 -*-
import json
import logging
import requests


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
