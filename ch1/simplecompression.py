#!/bin/python3
# -*- coding: utf-8 -*-
import sys
"""
 FileName : simplecompression.py
 Author : hongda
"""


"""简单的压缩算法, 通过核苷酸（ACGT）串的压缩存储描述压缩的原理"""


class SimpleCompress():

    def __init__(self, origin):
        self._compress(origin)

    def _compress(self, origin):
        self.bit_string = 1
        for word in origin.upper():
            self.bit_string <<= 2
            if word == 'A':
                self.bit_string |= 0b00
            elif word == 'C':
                self.bit_string |= 0b01
            elif word == 'G':
                self.bit_string |= 0b10
            elif word == 'T':
                self.bit_string |= 0b11
            else:
                raise ValueError("Invalid word:{}".format(word))

    def decompress(self):
        recvstr = ""
        for i in range(0, self.bit_string.bit_length()-1, 2):
            bit = self.bit_string >> i & 0b11
            if bit == 0b00:
                recvstr += 'A'
            elif bit == 0b01:
                recvstr += 'C'
            elif bit == 0b10:
                recvstr += 'G'
            elif bit == 0b11:
                recvstr += 'T'
            else:
                raise ValueError("Invalid bit:{}".format(bit))
        return recvstr

    def __str__(self):
        return self.decompress()[::-1]


if __name__ == "__main__":
    origin_str = "ACGT"*200
    print(origin_str)
    print("origin_str size is :", sys.getsizeof(origin_str))
    compress = SimpleCompress(origin_str)
    print("compress size is :", sys.getsizeof(compress))
    print(compress)
