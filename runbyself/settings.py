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
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive',
    'User-Agent': randUserAgent(),
        }
