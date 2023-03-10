import json
from utils.utils import request


class Client(object):
    def __init__(self, juejin_cookie, uuid):
        self.cookie = juejin_cookie
        self.uuid = uuid

    """
     发布沸点
    """

    def publish_pin(self, content, topic_id, theme_id):
        url = "https://api.juejin.cn/content_api/v1/short_msg/publish?aid=2608&uuid=" + self.uuid + "&spider=0"
        headers = {
            'authority': 'api.juejin.cn',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36',
            'content-type': 'application/json',
            'accept': '*/*',
            'origin': 'https://juejin.cn',
            'referer': 'https://juejin.cn/',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cookie': self.cookie
        }

        payload = {
            "content": content,
            "topic_id": topic_id,
            "sync_to_org": False,
            "theme_id": theme_id
        }
        resp = request("POST", url, headers, payload)
        return resp

    """
    发布草稿箱文章
    """

    def publish_article(self, draft_id, column_ids):
        url = "https://api.juejin.cn/content_api/v1/short_msg/publish?aid=2608&uuid=" + self.uuid
        headers = {
            'Cookie': self.cookie,
            'content-type': 'application/json',
            'accept': '*/*',
            'accept-language': 'zh-cn',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6.1 Safari/605.1.15'
        }

        payload = {
            "draft_id": draft_id,
            "sync_to_org": False,
            "column_ids": column_ids
        }
        resp = request("POST", url, headers, payload)
        return resp
