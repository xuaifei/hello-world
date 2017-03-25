# -*- coding: utf-8 -*-
'''this script common functions used by others '''
import functools
import sys


def seperator(line):
    print 'LINE', line, '================================='


def log(*text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print 'BEGIN:%s %s()%d:' \
                % (text[0], func.__name__,  sys._getframe().f_lineno)
            a = func(*args, **kw)
            print 'AFTER:%s %s()%d:' \
                % (text[0], func.__name__, sys._getframe().f_lineno)
            return a
        return wrapper
    return decorator
