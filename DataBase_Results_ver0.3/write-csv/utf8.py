#!/usr/bin/python2
# -*- coding: utf-8 -*-

import unicodecsv as ucsv
data = [[u"列1", u"列2"], [u"内容1", u"内容2"]]
with open('test.csv', 'wb') as f:
    w = ucsv.writer(f, encoding = 'utf-8')
    w.writerows(data)
