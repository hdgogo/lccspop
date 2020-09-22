#!/bin/python3
# -*- coding: utf-8 -*-
"""
 FileName : calculating_pi.py
 Author : hongda
"""


"""通过布莱尼茨公司计算PI"""


def calculate_pi(n_terms):
    numerator = 4.0
    denominator = 1.0
    operation = 1.0
    pi = 0.0
    for _ in range(n_terms):
        pi += operation * (numerator / denominator)
        denominator += 2.0
        operation *= -1.0
    return pi


if __name__ == '__main__':
    print(calculate_pi(100000000))
