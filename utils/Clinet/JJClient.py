# -*- coding: UTF-8 -*-
import json
import logging

from api.juejinApi import Client
from config import config

# init api client
JJClinet = Client(config.JUEJIN_COOKIE, config.JUEJIN_UUID)


def publish_article(draft_id):
    column_ids = list()
    response = JJClinet.publish_article(draft_id, column_ids)
    logging.debug(response.json)
    logging.debug(response.content)
    logging.debug(response.json())
    ret = json.loads(response.text)
    logging.debug(json.loads(response.text))
    return ret.get("err_no") == 0 and ret.get("err_msg") == "success"


def publish_pin(content, topic_id, theme_id):
    ret = JJClinet.publish_article(content, topic_id, theme_id).json
    return ret.get("err_no") == 0 and ret.get("err_msg") == "success"
