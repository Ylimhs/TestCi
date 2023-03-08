

# -*- coding: UTF-8 -*-
from api import githubApi
from config import config
import json
import logging
from datetime import datetime

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(format=LOG_FORMAT, level=logging.INFO)

import os
logging.info(os.getcwd())


def test():
    # init api client
    client = githubApi.Client(config.GIHHUB_BASEURL, config.GITHUB_OWNER, config.GITHUB_REPO, config.GITHUB_TOKEN)

    ret = client.list_repository_issues()
    logging.info("ret is : %s" , ret)




if __name__ == "__main__":
    test()
