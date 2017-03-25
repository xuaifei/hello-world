# -*- coding: utf-8 -*-
'''this script test python generator'''


def odd():
    print 'step 1'
    yield 1
    print 'step 2'
    yield 3
    print 'step 3'
    yield 5


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1


if __name__ == '__main__':
    L = range(1, 10)
    print L
    L = [n * n for n in range(10)]
    print L

    # 生成器 区别是(), 生成器可以一边生成一边用，而list可能一下子生成出来，占用内存太多
    print '================================================================'
    g = (n * n for n in range(2))
    print g
    # print "g.next()=", g.next()
    # print "g.next()=", g.next()
    # print g.next()
    for n in g:
        print "123:", n

    # yield
    print '================================================================'
    o = odd()
    print o.next()
    print o.next()
    print o.next()

    print '================================================================'
    for i in fib(10):
        print i