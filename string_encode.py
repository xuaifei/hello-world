# -*- coding:utf-8 -*-
"""this file test pyton string and coding"""

if __name__ == '__main__':
    print ord('A')
    print chr(65)

    # '中文'是Unicode字符,但是存在文本中是utf8编码
    print u'中文'

    # Unicode字符 转换成'\xe4\xb8\xad\xe6\x96\x87'
    print u'中文'.encode('utf-8')

    # ‘中文’的utf-8编码
    print '\xe4\xb8\xad\xe6\x96\x87'

    # 两个unicode字符
    print len(u'中文')

    # 把 utf-8的字符串转换成Unicode字符串 u'XXX'
    print '\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')