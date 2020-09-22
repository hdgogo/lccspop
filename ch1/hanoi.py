#!/bin/python3
# -*- coding: utf-8 -*-
"""
 FileName : hanoi.py
 Author : hongda
"""


'''解决汉诺塔问题'''


class Stack():
    """通过list完成栈的实现"""

    def __init__(self):
        self._container = []

    def push(self, item):
        self._container.append(item)

    def pop(self):
        return self._container.pop()

    def __repr__(self):
        return repr(self._container)


num_discs = 3
tower_a = Stack()
tower_b = Stack()
tower_c = Stack()

for i in range(1, num_discs+1):
    tower_a.push(i)


def hanoi(begin, end, temp, n):
    if n == 1:
        end.push(begin.pop())
    else:
        '''
        1、将上层n-1个圆盘从塔A(begin),移动到塔B(temp), 用塔C作为中转塔(end)
        2、将底层的圆盘从塔A(begin), 移动到塔C(end)
        3、将n-1个圆盘从塔B(temp)移动到塔C(end), 用塔A(begin)作为中转塔
        '''
        hanoi(begin, temp, end, n-1)
        hanoi(begin, end, temp, 1)
        hanoi(temp, end, begin, n-1)


if __name__ == "__main__":
    hanoi(tower_a, tower_c, tower_b, num_discs)
    print(tower_a)
    print(tower_b)
    print(tower_c)
