#! /usr/bin/env python3


from time import sleep


from selenium import webdriver
from selenium.common.exceptions import *



class BrowserOperation:

    def openBrowser(self):
        options = webdriver.ChromeOptions()
        options.add_argument('-no-sandbox')
        #  options.add_argument('-headless')
        self.driver = webdriver.Chrome(chrome_options=options)


    def wxoperation(self):
        if 'driver' not in self.__dict__:
            self.openBrowser()


        self.driver.get('https://mp.weixin.qq.com/')
        self.driver.find_element_by_name('account').send_keys('funnyimg')
        self.driver.find_element_by_name('password').send_keys('jjjYYl888')
        self.driver.find_element_by_xpath('//a[@title="点击登录"]').click()
        sleep(5)
        try:
            self.driver.find_element_by_xpath('//div[@class="weui-desktop-global__extra"]/a').click()
        except (StaleElementReferenceException, NoSuchElementException):
            sleep(5)
            self.driver.find_element_by_xpath('//div[@class="weui-desktop-global__extra"]/a').click()
        self.driver.switch_to.window(self.driver.window_handles[-1])

        sleep(20)
        self.driver.find_elements_by_class_name('create-type__item')[1].click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        sleep(20)
        self.driver.find_element_by_id('js_editor_insertlink').click()
        sleep(2)

        self.wxcookies = self.driver.get_cookies()


    def wxcookieParse(self):
        print(cstring)
        return cstring

    def wxtoken(self):
        self.


    def getPastArg(self):
        cookie = ''
        for c in self.wxcookies:
            cookie += c['name'] + '=' + c['value'] + ';'
        for t in self.current_url.split('&'):
            if t.startswith('token='):
                token = t.split('=')[1]
                break
        return token, cookie






if __name__ == "__main__":
    b = BrowserOperation()
    b.wxoperation()
    from extract import getPast
    r = getPast(b.getPastArg())
    print(r)



