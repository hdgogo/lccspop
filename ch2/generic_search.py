#!/bin/python3
# -*- coding: utf-8 -*-
"""
 FileName : generic_search.py
 Author : hongda
"""

from collections import deque
from heapq import heappush, heappop


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
    """栈的实现, 用于深度优先搜索"""

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


class Queue():
    """队列的实现, 用于广度优先搜索"""

    def __init__(self):
        self._container = deque()

    @property
    def empty(self):
        return not self._container

    def push(self, item):
        self._container.append(item)

    def pop(self):
        return self._container.popleft()

    def __repr__(self):
        return repr(self._container)


class PriorityQueue():
    """优先队列的实现， 用于A*搜索"""

    def __init__(self):
        self._container = []

    @property
    def empty(self):
        return not self._container

    def push(self, item):
        heappush(self._container, item)

    def pop(self):
        return heappop(self._container)

    def __repr__(self):
        return repr(self._container)


class Node():
    """对于状态的封装， 用于记录搜索时记录从一种状态到另一种状态的过程"""

    def __init__(self, state, parent, cost=0.00, heuristic=0.00):
        self.state = state
        self.parent = parent
        """成本， 用于A* 搜索"""
        self.cost = cost
        """启发式信息, 旨在选取下一次搜索的最佳位置"""
        self.heuristic = heuristic

    def __lt__(self, other):
        """因为 PriorityQueue 使用heappush和heappop ， 而上诉操作使用”<“进行比较, 故实现__lt__方法"""
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)


def dfs(initinal, goal_test, successors):
    """深度优先搜索"""
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


def bfs(initinal, goal_test, successors):
    """广度优先搜索"""
    frontier = Queue()  # 当前要搜索的状态栈
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


def astart(initinal, goal_test, successors, heuristic):
    """A*搜索"""
    frontier = PriorityQueue()
    frontier.push(Node(initinal, None, 0.00, heuristic(initinal)))

    explored = {initinal: 0.00}

    while not frontier.empty:
        current_node = frontier.pop()
        current_state = current_node.state

        if goal_test(current_state):
            return current_node

        for child in successors(current_state):
            new_cost = current_node.cost + 1

            if child not in explored or explored[child] > new_cost:
                explored[child] = new_cost
                frontier.push(Node(child, current_node,
                                   new_cost, heuristic(child)))

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
