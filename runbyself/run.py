#!/usr/bin/env python3

from extract import *
from editing import editor
from broperation import BrowserOperation




if __name__ == "__main__":

    f = open('caching.txt', 'r+').readline().strip()
    bo = BrowserOperation()
    bo.wxoperation()
    initdata = origin(int(f))
    result = parse(initdata)
    token, cookie = bo.getPastArg()
    editor(result, token, cookie)
