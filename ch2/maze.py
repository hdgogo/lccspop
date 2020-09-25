#!/bin/python3
# -*- coding: utf-8 -*-
"""
 FileName : maze.py
 Author : hongda
"""


from enum import Enum
import random
from math import sqrt
from collections import namedtuple
from generic_search import dfs, bfs, node_to_path, astart


class Cell(str, Enum):
    EMPTY = ' '
    BLOCKED = 'X'
    START = 'S'
    GOAL = 'G'
    PATH = '*'


MazeLocation = namedtuple('MazeLocation', ('row', 'column'))


class Maze:
    def __init__(self, rows=10, columns=10, sparseness=0.1, start=MazeLocation(0, 0), goal=MazeLocation(9, 9)):
        self._rows = rows
        self._columns = columns
        self.start = start
        self.goal = goal
        # 使用空串填充迷宫表格
        self._grid = [[Cell.EMPTY for c in range(
            columns)] for r in range(rows)]
        # 通过sparseness参数随机填充迷宫Cell.BLOCKED
        self._randomly_file(rows, columns, sparseness)
        # 添加开始和目标节点
        self._grid[start.row][start.column] = Cell.START
        self._grid[goal.row][goal.column] = Cell.GOAL

    def _randomly_file(self, rows, columns, sparseness):
        for row in range(rows):
            for column in range(columns):
                if random.uniform(0, 1.0) < sparseness:
                    self._grid[row][column] = Cell.BLOCKED

    def __str__(self):
        """打印迷宫"""
        output = ""
        for row in self._grid:
            output += "".join([c for c in row])+"\n"
        return output

    def goal_test(self, ml):
        """判断是否到达目标"""
        return ml == self.goal

    def successors(self, ml):
        """判断当前ml可以前进的位置"""
        locations = []
        if ml.row + 1 < self._rows and self._grid[ml.row + 1][ml.column] != Cell.BLOCKED:
            locations.append(MazeLocation(ml.row+1, ml.column))
        if ml.row - 1 > 0 and self._grid[ml.row - 1][ml.column] != Cell.BLOCKED:
            locations.append(MazeLocation(ml.row-1, ml.column))
        if ml.column + 1 < self._columns and self._grid[ml.row][ml.column + 1] != Cell.BLOCKED:
            locations.append(MazeLocation(ml.row, ml.column+1))
        if ml.column - 1 > 0 and self._grid[ml.row][ml.column - 1] != Cell.BLOCKED:
            locations.append(MazeLocation(ml.row, ml.column-1))
        return locations

    def mark(self, path):
        for mazeLocation in path:
            self._grid[mazeLocation.row][mazeLocation.column] = Cell.PATH
        self._grid[self.start.row][self.start.column] = Cell.START
        self._grid[self.goal.row][self.goal.column] = Cell.GOAL

    def clear(self, path):
        for mazeLocation in path:
            self._grid[mazeLocation.row][mazeLocation.column] = Cell.EMPTY
        self._grid[self.start.row][self.start.column] = Cell.START
        self._grid[self.goal.row][self.goal.column] = Cell.GOAL


def euclidean_distance(goal):
    """欧几里德距离"""
    def distance(ml):
        x = ml.row - goal.row
        y = ml.column - goal.column

        return sqrt(x * x + y * y)
    return distance


def manhattan_distance(goal):
    """曼哈顿距离"""
    def distance(ml):
        x = abs(ml.row - goal.row)
        y = abs(ml.column - goal.column)

        return x + y
    return distance


if __name__ == '__main__':
    m = Maze()
    print(m)

    solution = dfs(m.start, m.goal_test, m.successors)

    if solution is None:
        print("No solution found using deepth-first search")
    else:
        path = node_to_path(solution)
        m.mark(path)
        print(m)
        m.clear(path)

    solution = bfs(m.start, m.goal_test, m.successors)

    if solution is None:
        print("No solution found using deepth-first search")
    else:
        path = node_to_path(solution)
        m.mark(path)
        print(m)
        m.clear(path)

    distance = manhattan_distance(m.goal)
    solution = astart(m.start, m.goal_test, m.successors, distance)

    if solution is None:
        print("No solution found using deepth-first search")
    else:
        path = node_to_path(solution)
        m.mark(path)
        print(m)
        m.clear(path)
