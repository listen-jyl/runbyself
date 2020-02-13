#!/usr/bin/env python3


from extract import getPast


def editor(data_json, token, cookie):
    html = '''
    <!doctype html>
    <html>
    <head><meta charset="utf-8"></head>
    <body>
    <section class="mpa-template" data-mpa-template="t">
        <img src="http://mmbiz.qpic.cn/mmbiz_gif/4RkGAHUQZDPQuZvzRpgMavjJcyYZw0HskqcZJRib59UzoicsxrL1PUE763GZaOPJmoeYg306jL42tcc04L5BtETA/0?map-referer=none" />
    </section>
    <section class="_editor" data-support="96编辑器" data-style-id="25866">
        <section style="margin:10px 0px;">
            <section style="border-style:solid; border-width: 2px; border-color: #5f93e9;  padding: 15px 15px 20px; box-sizing: border-box;margin-right:10px;">
                <p style="letter-spacing: 2px;">
                    <span style="font-size: 15px; color: #5c5c5c;">文章内容素材均来源于网络</span>
                </p>
            </section>
        </section>
    </section>
    <br><br>
    '''

    for data in data_json:
        template = '''
        <section class="_editor"  data-style-id="25103">
            <section style="margin:10px 0px;">
                <section style="padding:20px; border-top:solid 5px #dc1105; border-bottom:solid 1px #87cefa; border-left:solid 1px #87cefa; border-right:solid 1px #87cefa;">
                    <section style="border-left:solid 2px #dc1105; height:auto; padding-left:5px;">
                        <p style="font-size: 0.9rem; color: #353535; letter-spacing: 2px;">
                            {title}<br/>
                        </p>
                    </section>
                    <section style="width:100%; margin-top:20px;" data-width="100%">
                        {imgtag}<br/>
                        <p style="font-size: 0.9rem; color: #353535; letter-spacing: 2px;">
                            {review}<br/>
                        </p>
                        {review_imgs}
                    </section>
                </section>
            </section>
        </section><br>
        '''
        template = template.replace('{title}', data['title'])
        imgtag = ''
        if not data['urls']:
            continue

        for url in data['urls']:
            imgtag += '<img style="display: block; width: 100%;" src="{url}"/><br>'.format(url=url)
        template = template.replace('{imgtag}', imgtag)
        if data['review_imgs']:
            template = template.replace("{review}", "<strong>神评:</strong>"+data['review'])
            review_imgs = ''
            for rurl in data['review_imgs']:
                review_imgs += '<img style="display: block; width: 100%;" src="{url}"/><br>'.format(url=rurl)
            template = template.replace("{review_imgs}", review_imgs)
        else:
            template = template.replace("{review}", '')
            template = template.replace("{review_imgs}", '')

        html += template

    tail = '''
    <section class="_editor" data-support="96编辑器" data-style-id="20126">
        <section style="margin-top: 10px;margin-bottom: 10px;text-align: center;font-size: 13px;box-sizing: border-box;">
            <section style="display: inline-block;vertical-align: top;box-sizing: border-box;">
                <section style="background-color: #fbfbfb;padding-right: 12px;padding-left: 12px;color: #7a3c36;box-sizing: border-box;">
                    <p style="clear: none;box-sizing: border-box;">
                        <strong style="box-sizing: border-box;">推 荐 阅 读</strong>
                    </p>
                </section>
                <section style="width: 6px;height: 6px;border-radius: 100%;float: left;margin-top: -14px;background-color: #000000;box-sizing: border-box;"></section>
                <section style="width: 6px;height: 6px;border-radius: 100%;float: right;margin-top: -14px;background-color: #000000;box-sizing: border-box;"></section>
                <section style="clear: both;box-sizing: border-box;"></section>
            </section>
            <section style="border-width: 1px;border-style: solid;border-color: #a0a0a0;margin-top: -12px;padding: 10px;border-radius: 0px;box-sizing: border-box;">
                <section style="margin-top: 5px;margin-right: 0%;margin-left: 0%;box-sizing: border-box;">
                    <p style="box-sizing: border-box; line-height: 2em;">
                        <a href="{rurl0}" target="_blank" style="text-decoration: underline;font-size: 14px;">
                        {rtitle0}
                        </a><br/>
                        <a href="{rurl1}" target="_blank" style="text-decoration: underline;font-size: 14px;">
                        {rtitle1}
                        </a><br/>
                        <a href="{rurl2}" target="_blank" style="text-decoration: underline;font-size: 14px;">
                        {rtitle2}
                        </a>
                    </p>
                </section>
            </section>
        </section>
    </section>

    </body></html>'''

    plist = getPast(token, cookie)
    tail = tail.replace('{rtitle0}', plist['rtitle0'])
    tail = tail.replace('{rtitle1}', plist['rtitle1'])
    tail = tail.replace('{rtitle2}', plist['rtitle2'])
    tail = tail.replace('{rurl0}', plist['rurl0'])
    tail = tail.replace('{rurl1}', plist['rurl1'])
    tail = tail.replace('{rurl2}', plist['rurl2'])

    html += tail


    f = open('/var/www/html/test.html', 'w')
    f.write(html)
    return html





if __name__ == "__main__":
    pass
