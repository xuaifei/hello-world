# -*- coding: utf-8 -*-
'''this script test python function'''
import sys
import utility

# note default vaule param should behind no default


def varFunc(*varPara):
    '''variable parameters, inner function varPara construct tuple'''
    sum = 0
    for i in varPara:
        sum = sum + i * i
    return sum


def dicFunc(name, age, **kw):
    """关键字参数, inner function argv construct to dict"""
    print "name:", name, ", age: ", age, ", other:", kw


def combFunc(a, b, c=0, *args, **kw):
    """顺序必须: 必选参数，默认参数，可变参数，关键字参数"""
    print 'a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw


def inputFunc(a, b, f):
    return f(a) + f(b)


def f(x):
    return x * x


def f1(x, y):
    return x + y


def refactor(string):
    return string.title()


def is_odd(n):
    return n % 2 == 1


def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    return sum


def log(func):
    def wrapper(*args, **kw):
        print 'call %s():' % func.__name__
        return func(*args, **kw)
    return wrapper


@utility.log(str(sys._getframe().f_lineno))
def now():
    print '2013-12-25'


if __name__ == '__main__':
    print varFunc(1, 2, 3)

    utility.seperator(sys._getframe().f_lineno)
    num = [1, 2, 3]
    print varFunc(*num)

    utility.seperator(sys._getframe().f_lineno)
    dicFunc("Bob", 36, city='Beijing')
    dicFunc('Adam', 45, gender='M', job='Engineer')

    utility.seperator(sys._getframe().f_lineno)
    kw = {"city": "Shenzhen", "job": "saler"}
    dicFunc("jack", 20, **kw)

    utility.seperator(sys._getframe().f_lineno)
    combFunc(1, 2, 3, 'a', 'b', x=99, y=10)
    args = (1, 2, 3, 4)
    kw = {'x': 99}
    combFunc(*args, **kw)

    utility.seperator(sys._getframe().f_lineno)
    print inputFunc(1, -1, abs)

    # map 是对序列里面的元素 执行函数，最终得到一个序列
    utility.seperator(sys._getframe().f_lineno)
    print map(f, range(10))
    print map(refactor, ['adam', 'LISA', 'barT'])

    # reduce 是对序列的第 1 ,2 个元素执行函数f1，结果对第三个元素执行f1，最终计算出一个结果
    utility.seperator(sys._getframe().f_lineno)
    print reduce(f1, range(10))

    utility.seperator(sys._getframe().f_lineno)
    print filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])

    utility.seperator(sys._getframe().f_lineno)
    print sorted([36, 5, 12, 9, 21])

    # 闭包
    utility.seperator(sys._getframe().f_lineno)
    f = lazy_sum(1, 3, 5, 7, 9)
    print f
    print f()

    # 匿名函数， lambda 后面的x是参数
    utility.seperator(sys._getframe().f_lineno)
    print map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])

    # 函数变量 名字 , 装饰器decorator:运行期间动态增加函数功能
    utility.seperator(sys._getframe().f_lineno)
    print lazy_sum.__name__
    tmpfun = lazy_sum
    print tmpfun.__name__
    now()
