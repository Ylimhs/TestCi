# -*- coding: UTF-8 -*-
import json
from utils.utils import request

class Client(object):
    def __init__(self, base_url, owner, repo, github_token):
        self.base_url = base_url
        self.owner = owner
        self.repo = repo
        self.github_token = github_token

    def list_repository_issues(self):
        url = self.base_url  + "/" + self.owner + "/" + self.repo + "/issues"
        headers = {
            'Accept': 'application/vnd.github+json',
            'Authorization': 'Bearer ' + self.github_token
        }
        resp = request("GET", url, headers)
        return resp.json()

    def create_repository_issues(self):
        url = self.base_url + "/" + self.owner + "/" + self.repo + "/issues"
        headers = {
            'Accept': 'application/vnd.github+json',
            'Authorization': 'Bearer ' + self.github_token
        }
        resp = request("GET", url, headers)
        return resp.json()

