#!/usr/bin/env python3


from os import path

import xlsxwriter

import settings
from tools import getResponse



class Save:
    def __init__(self):

        self.save_path = settings.SAVE_PATH
        self._maps = set()


    def saveImg(self, url, imgname, fil=True):
        if fil:
            if url not in self._maps:
                res = getResponse(url, tree=0)
                #  print(res.content)
                with open(path.join(settings.IMG_SAVE_DIR, imgname), 'wb') as img:
                    img.write(res.content)
                return self
        else:
            res = getResponse(url, tree=0)
            with open(path.join(settings.IMG_SAVE_DIR, imgname, 'wb')) as img:
                img.write(res.content)
            return self


    def createSheet(self):

        self.book = xlsxwriter.Workbook(self.save_path+'.xlsx')
        self.sheet = self.book.add_worksheet()
        return self


    def createText(self):

        self.textfile = open(self.save_path+'.txt', 'w')
        return self


    def saveStr(self, item, skip_error_type=False, fil=True):
        if type(item) == str:
            if 'textfile' not in self.__dict__:
                self.createText()

            if fil:
                if item not in self._maps:
                    self.textfile.write(item+'\n')
                    self._maps.add(item)
            else:
                self.textfile.write(item+'\n')

        elif type(item) == list:
            self.saveList(item, fil=fil)

        elif type(item) == dict:
            self.saveDict(item, fil=fil)

        else: self.__exception('请传入正确数据类型', skip_error_type)


    def __exception(self, tips, skip=False):
        if skip: pass
        else: raise TypeError(tips)
        return self


    def saveList(self, item, skip_error_type=False, fil=True):
        for i in item:
            if type(i) == str:
                self.saveStr(i, fil=fil)

            elif type(i) == dict:
                self.saveDict(i, fil=fil)

            else: self.__exception('请传入正确数据类型', skip_error_type)


    def __saveDict(self, item):
        ik = item.keys()
        if ik == self.field:
            for i in range(len(ik)):
                self.sheet.write(self.__lastrow, i, item[self.__lfield[i]])
            self.__lastrow += 1
            return self


    def saveDict(self, item, skip_error_type=False, fil=True):
        if type(item) == dict:
            if 'book' not in self.__dict__ or 'sheet' not in self.__dict__:
                self.createSheet()

            if 'field' not in self.__dict__:
                self.field = item.keys()
                self.__lfield = list(self.field)
                for e, i in enumerate(self.field):
                    self.sheet.write(0, e, i)
                self.__lastrow = 1

            if fil:
                if item not in self._maps:
                    self.__saveDict(item)
                    self._maps.add(item)
            else:
                self.__saveDict(item)


        elif type(item) == str:
            self.saveStr(item, fil=fil)

        elif type(item) == list:
            self.saveList(item, fil=fil)

        else: self.__exception('请传入正确数据类型', skip_error_type)


    def close(self):
        try:
            self.book.close()
            self.textfile.close()
        except:
            pass
        return self


if __name__ == "__main__":
    s = Save()
    #  s.saveStr('123123123')
    #  s.saveDict({'a':1, 'b':2})
    #  s.saveDict([{'a':2, 'b':3}, {'a':33, 'b':33}, {'a':44, 'b':111}, {'b':'bbb', 'a':'aaa'}])
    #  s.saveStr('123123123', fil=False)
    #  s.saveDict('18888823')

    s.saveImg("http://jd-tv.com/uploads/allimg/191106/18-191106100323G3.jpg", 'test')




    s.close()






