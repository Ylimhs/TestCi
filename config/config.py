# -*- coding: UTF-8 -*-
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

# load from env
GIHHUB_BASEURL =os.getenv("GIHHUB_BASEURL")
GITHUB_OWNER = os.getenv("GITHUB_OWNER")
GITHUB_REPO = os.getenv("GITHUB_REPO")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

# ACCEPT = "Accept: application/vnd.github+json"