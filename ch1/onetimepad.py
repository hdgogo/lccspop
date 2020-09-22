#!/bin/python3
# -*- coding: utf-8 -*-
"""
 FileName : onetimepad.py
 Author : hongda
"""


from secrets import token_bytes


def random_key(length):
    # 生成指定长度的随机密钥
    tb = token_bytes(length)
    return int.from_bytes(tb, "big")


def encrypt(original):
    """通过XOR运算进行加密"""
    original_bytes = original.encode()
    dummy = random_key(len(original_bytes))
    original_key = int.from_bytes(original_bytes, "big")
    encrypted = original_key ^ dummy
    return dummy, encrypted


def decrypt(key1, key2):
    decrypted = key1 ^ key2
    temp = decrypted.to_bytes((decrypted.bit_length()+7) // 8, "big")
    return temp.decode()


if __name__ == '__main__':
    key1, key2 = encrypt("这是一个明文!")
    result = decrypt(key1, key2)
    print("解密后的原文为:{}".format(result))
