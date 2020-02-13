#!/usr/bin/env python3


import json

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
            item['urls'] = []
            for u in i['imgs']:
                if u['fmt'] != 'jpeg':
                    continue
                item['urls'].append(u['urls']['origin']['urls'][0])

            item['reviews'] = i['reviews']
            item['up'] = i['up']
            item['down'] = i['down']
            item['title'] = i['content']
            item['likes'] = i['likes']
            item['review_imgs'] = []
            god_reviews = i['god_reviews']
            if god_reviews:
                for u in god_reviews[0]['imgs']:
                    if u['fmt'] != 'jpeg':
                        continue
                    item['review_imgs'].append(u['urls']['origin']['urls'][0])
                if item['review_imgs']:

                    item['review'] = god_reviews[0]['review']
                    item['subreviewcnt'] = god_reviews[0]['subreviewcnt']
                    #  item['review_imgs'] = god_reviews[0]['imgs']

                    item['review_up'] = god_reviews[0]['up']
                    item['review_down'] = god_reviews[0]['down']
                    item['review_likes'] = god_reviews[0]['likes']
        except:
            continue

        result.append(item)
    return result


def origin(page):
    url = 'http://izuiyou.com/api/index/webrecommend'

    data = {"h_av":"3.0","h_dt":9,"h_nt":9,"h_ch":"web_app","ua":"Mozilla/5.0 (X11; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0","ctn":20,"direction":"up","tab":"rec","offset":0,"filter":"all"}
    data['offset'] = page
    return getResponse(url=url, method="post", headers=HEADERS, data=json.dumps(data))


def getPast(token, cookies):
    url = "https://mp.weixin.qq.com/cgi-bin/appmsg?action=list_ex&begin=0&count=5&fakeid=&type=9&query=&token=412561177&lang=zh_CN&f=json&ajax=1"
    headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0",
            'Cookie': cookies,
            }

    res = getResponse(url=url, headers=headers)
    jdata = json.loads(res)

    result = {}
    result['rtitle0'] = jdata['app_msg_list'][0]['title']
    result['rtitle1'] = jdata['app_msg_list'][1]['title']
    result['rtitle2'] = jdata['app_msg_list'][2]['title']

    result['rurl0'] = jdata['app_msg_list'][0]['link']
    result['rurl1'] = jdata['app_msg_list'][1]['link']
    result['rurl2'] = jdata['app_msg_list'][2]['link']


    return result





if __name__ == "__main__":
    getPast()
    #  spider(20)


















