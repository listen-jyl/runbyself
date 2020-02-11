#!/usr/bin/env python3


import json
import requests
from lxml import etree


from tools import *


def parse(json_data):
    try:
        if type(json_data) == str:
            json_data = json.loads(json_data)
    except:
        print("传入数据类型错误")
        return
    result = []
    for i in json_data['data']['list']:
        item = {}
        try:
            #  item['urls'] =  i['imgs'][0]['urls']['origin']['urls']
            item['urls'] = []
            for u in i['imgs']:
                item['urls'].append(u['urls']['origin']['urls'][0])
            item['reviews'] = i['reviews']
            item['up'] = i['up']
            item['down'] = i['down']
            item['title'] = i['content']
            item['likes'] = i['likes']
            god_reviews = i['god_reviews']
            if god_reviews:
                item['review'] = god_reviews[0]['review']
                item['subreviewcnt'] = god_reviews[0]['subreviewcnt']
                #  item['review_imgs'] = god_reviews[0]['imgs']
                item['review_imgs'] = []
                for u in god_reviews[0]['imgs']:
                    item['review_imgs'].append(u['urls']['origin']['urls'][0])

                item['review_up'] = god_reviews[0]['up']
                item['review_down'] = god_reviews[0]['down']
                item['review_llike'] = god_reviews[0]['likes']
        except:
            continue

        result.append(item)
    print(result, len(result))







def spider(page):
    url = 'http://izuiyou.com/api/index/webrecommend'

    data = {"h_av":"3.0","h_dt":9,"h_nt":9,"h_ch":"web_app","ua":"Mozilla/5.0 (X11; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0","ctn":20,"direction":"up","tab":"rec","offset":0,"filter":"all"}
    data['offset'] = page

    res = getResponse(url=url, tree=0, method="post", headers=HEADERS, data=json.dumps(data))
    parse(res.text)




if __name__ == "__main__":
    spider(0)


















