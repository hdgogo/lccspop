#!/bin/python3
# -*- coding: utf-8 -*-
from functools import lru_cache
"""
 FileName : fib1.py
 Author : hongda
"""

"""
生成斐波那契序列
0 1 1 2 3 5 8 13 21 .....
"""


def fib(n):
    # “指定基线条件，明确结束递归”
    if n < 2:
        return n
    """
    递归算法，
    此处存在效率问题，如果指定的数很大，会运算很长时间
    例如计算n=4 的序列，鸠需要调用fib函数9次
    fib(4)  = fib(3) + fib(2)
    fib(3)  = fib(2) + fib(1)
    fib(2)  = fib(1) + fib(0)
    fib(2)  = fib(1) + fib(0)
    fib(1)  = 1
    fib(1)  = 1
    fib(1)  = 1
    fib(0)  = 0
    fib(0)  = 0
    """
    return fib(n-1) + fib(n-2)


""" 初始的契波那契序列 """
init_db = {0: 0, 1: 1}


def fib_withdb(n):
    """通过缓存优化上面的方法，减少函数的调用"""
    if n not in init_db:
        init_db[n] = fib_withdb(n-1) + fib_withdb(n-2)  # 添加缓存
    return init_db[n]


"""通过python自带的lru_cache 缓存结果， 减少函数的调用"""
@lru_cache(maxsize=None)
def fib_cache(n):
    if n < 2:
        return n
    return fib_cache(n-1) + fib_cache(n-2)


def fib_no_recursion(n):
    """不使用递归完成契波那契序列"""
    if n == 0:
        return n
    last = 0  # 初始化fib_no_recursion(0)
    next = 1  # 初始化fib_no_recursion(1)
    for _ in range(1, n):
        last, next = next, last+next
    return next


def fib_generator(n):
    """契波那契序列生成器"""
    yield(0)
    if n > 0:
        yield 1
    last = 0
    next = 1
    for _ in range(1, n):
        last, next = next, last+next
        yield next


if __name__ == '__main__':
    for i in range(0, 10):
        print(fib(i), end=' ')
    print()
    for i in range(0, 50):
        print(fib_withdb(i), end=' ')
    print()
    for i in range(0, 50):
        print(fib_cache(i), end=' ')
    print()
    for i in range(0, 50):
        print(fib_no_recursion(i), end=' ')
    print()

    for i in fib_generator(50):
        print(i, end=' ')
    print()
