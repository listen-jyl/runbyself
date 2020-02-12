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


def getPast():
    url = "https://mp.weixin.qq.com/cgi-bin/appmsg?action=list_ex&begin=0&count=5&fakeid=&type=9&query=&token=412561177&lang=zh_CN&f=json&ajax=1"
    headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0",
            "Cookie": "pgv_pvid=5205276349; pac_uid=0_5e3e5d8168736; ua_id=MmKqjAdWimsBkpbSAAAAAN0ovwEGFovcHicyK9QtwBY=; pgv_pvi=8545026048; bizuin=3584818375; noticeLoginFlag=1; xid=0f7e993190b2ab840d17fabbd51d1c47; openid2ticket_ox_yr1XXmqC6SvZaU5WcRfnX2cFU=bNpyvhmcGQkQLkwb7jmZyYnMSVHu984phPEOa7p+eog=; mm_lang=zh_CN; pgv_si=s7447269376; uuid=7d06108ba4db2ac65f5c92a7ee900c67; ticket=363d741e57fc135969268eebd02d37d13e047de2; ticket_id=gh_b87daea82ca8; cert=bOooa_XCrRzua9_OXhGmuZgrq5_sSXWb; data_bizuin=3584818375; data_ticket=x9Pa90TD5Br5YwkguXEVel2ZzRR06qmCB1cS02SFAqN6bbpmeA3hCMITi9451Ww7; slave_sid=bXMzdG9iY2wybEw5ZVdXcDBCa3QzdlNuVFRjY3BJY24xQTJqODJROWN0akZZNVNKWlFodzJGVGJ6RjBOcTJSWE1GNGNjVUw5NU1UQ1FqRFBabHJtNXVBeExwc3d0dlJPS2l6enl6aWdYYkdTWDFfUG1uM2xidks1Tmw0cTBRbWEwb0lWVzlDUWRud29VVzlV; slave_user=gh_b87daea82ca8; rewardsn=; wxtokenkey=777"
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


















