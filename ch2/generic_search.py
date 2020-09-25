#!/bin/python3
# -*- coding: utf-8 -*-
"""
 FileName : generic_search.py
 Author : hongda
"""


def linear_contains(iterable, key):
    """线性搜索"""
    for item in iterable:
        if key == item:
            return True
    return False


def binary_contains(sequence, key):
    low = 0
    high = len(sequence) - 1
    while low <= high:
        mid = low+high // 2
        if sequence[mid] < key:
            low = mid + 1
        elif sequence[mid] > key:
            high = mid - 1
        else:
            return True
    return False


class Stack():
    """栈的实现"""

    def __init__(self):
        self._container = []

    @property
    def empty(self):
        return not self._container

    def push(self, item):
        self._container.append(item)

    def pop(self):
        return self._container.pop()

    def __repr__(self):
        return repr(self._container)


class Node():
    """对于状态的封装， 用于记录搜索时记录从一种状态到另一种状态的过程"""

    def __init__(self, state, parent, cost=0.00, heuristic=0.00):
        self.state = state
        self.parent = parent
        self.cost = cost
        self.heuristic = heuristic

    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)


def dfs(initinal, goal_test, successors):
    """深度搜索"""
    frontier = Stack()  # 当前要搜索的状态栈
    frontier.push(Node(initinal, None))

    explored = {initinal}  # 已搜索过的状态栈

    while not frontier.empty:
        current_node = frontier.pop()
        current_state = current_node.state

        if goal_test(current_state):
            return current_node

        for child in successors(current_state):
            if child in explored:
                continue
            explored.add(child)
            frontier.push(Node(child, current_node))

    return None


def node_to_path(node):
    """绘制搜索路径"""
    path = []
    path.append(node.state)
    while node.parent:
        node = node.parent
        path.append(node.state)
    path.reverse()
    return path
