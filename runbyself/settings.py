#!/usr/bin/env python3


from os import path
from datetime import datetime

from tools import randUserAgent


#爬取的url
START_URL = 'https://jx.911cha.com/'


#储存数据的路径
SAVE_DIR = '/data'


#图片储存路径
IMG_SAVE_DIR = path.join(SAVE_DIR, "imgs")


####################################
#没事别乱改，使用默认的就可以了
domain = START_URL.split(".")
SPIDER_NAME = domain[1].title() if 'www' in START_URL or 'http' in START_URL else domain[0].title()
SAVE_PATH = path.join(SAVE_DIR,  SPIDER_NAME + datetime.now().strftime('%m%d%H%M%s')[:10])
####################################


#线程数
THREADS = 20


#自定义请求头
HEADERS = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh,zh-TW;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6',
    'Connection': 'keep-alive',
    'Content-Length': 236,
    'Content-Type': 'text/plain;charset=UTF-8',
    'Host': 'www.izuiyou.com',
    'Origin': 'https://www.izuiyou.com',
    'Referer': 'https://www.izuiyou.com/',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': randUserAgent(),
        }
