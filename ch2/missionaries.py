#!/bin/python3
# -*- coding: utf-8 -*-
"""
 FileName : missionaries.py
 Author : hongda
"""


from generic_search import bfs, Node, node_to_path

MAX_NUM = 3


class MCState():

    def __init__(self, missionaries, cancibals, boat):
        """
        missionaries : 西岸传教士数量
        cancibals   : 西岸食人族熟练
        boat        : 船是否在西岸
        """
        self.wm = missionaries
        self.wc = cancibals
        self.em = MAX_NUM - self.wm
        self.ec = MAX_NUM - self.wc
        self.boat = boat

    def __str__(self):
        return "在西岸有{}个传教士和{}个食人族.\n"\
            "在东岸有{}个传教士和{}个食人族。\n"\
            "船在{}岸".format(self.wm, self.wc, self.em, self.ec,
                           ("西" if self.boat else "东"))

    def goal_test(self):
        return self.is_legal and self.em == MAX_NUM and self.ec == MAX_NUM

    @property
    def is_legal(self):
        if self.wm < self.wc and self.wm > 0:
            return False
        if self.em < self.ec and self.em > 0:
            return False
        return True

    def successord(self):
        sucs = []
        if self.boat:  # boat on west bank
            if self.wm > 1:
                sucs.append(MCState(self.wm - 2, self.wc, not self.boat))
            if self.wm > 0:
                sucs.append(MCState(self.wm - 1, self.wc, not self.boat))
            if self.wc > 1:
                sucs.append(MCState(self.wm, self.wc - 2, not self.boat))
            if self.wc > 0:
                sucs.append(MCState(self.wm,  self.wc - 1, not self.boat))
            if (self.wc > 0) and (self.wm > 0):
                sucs.append(MCState(self.wm-1, self.wc - 1, not self.boat))
        else:  # boat on east bank
            if self.em > 1:
                sucs.append(MCState(self.wm + 2, self.wc, not self.boat))
            if self.em > 0:
                sucs.append(MCState(self.wm + 1, self.wc, not self.boat))
            if self.ec > 1:
                sucs.append(MCState(self.wm, self.wc+2, not self.boat))
            if self.ec > 0:
                sucs.append(MCState(self.wm, self.wc+1, not self.boat))
            if (self.ec > 0) and (self.em > 0):
                sucs.append(MCState(self.wm+1, self.wc + 1, not self.boat))

        return [x for x in sucs if x.is_legal]


def display_solution(path):
    if len(path) == 0:
        return
    old_state = path[0]
    print(old_state)
    for current_state in path[1:]:
        if current_state.boat:
            print("{}个传教士和{}个食人族从东岸去西岸。\n".format(old_state.em -
                                                  current_state.em, old_state.ec - current_state.ec))
        else:
            print("{}个传教士和{}个食人族从西岸去东岸。\n".format(old_state.wm -
                                                  current_state.wm, old_state.wc - current_state.wc))
        print(current_state)
        old_state = current_state


if __name__ == '__main__':
    start = MCState(MAX_NUM, MAX_NUM, True)
    solution = bfs(start, MCState.goal_test, MCState.successord)

    if solution is None:
        print("No solution found ! ")
    else:
        path = node_to_path(solution)
        display_solution(path)
