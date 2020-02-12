#!/usr/bin/env python3

from extract import origin, parse
from editing import editor


f = open('caching.txt', 'r+').readline().strip()


initdata = origin(int(f))
result = parse(initdata)
editor(result)
