#!/bin/python3
# -*- coding: utf-8 -*-
"""
 FileName : dns_search.py
 Author : hongda
"""


from enum import IntEnum

Nucleotide = IntEnum('Nucleotide', ('A', 'C', 'G', 'T'))

gene_str = "ACGTGGCTCTCTAACGTAGGTACGGGGTTTATAATACCCTAGGACTCCCTTT"


def str_to_gene(s):
    gene = []
    for i in range(0, len(s), 3):
        if i+2 >= len(s):
            return gene
        codon = (Nucleotide[s[i]], Nucleotide[s[i+1]], Nucleotide[s[i+2]])
        gene.append(codon)
    return gene


my_gene = str_to_gene(gene_str)


def linear_contains(gene, key_codon):
    """线性搜索"""
    for code in gene:
        if key_codon == code:
            return True
    return False


def binary_contains(gene, key_codon):
    """二分查找"""
    low = 0
    high = len(gene) - 1
    while low <= high:
        mid = (low + high) // 2
        if gene[mid] < key_codon:
            low = mid+1
        elif gene[mid] > key_codon:
            high = mid - 1
        else:
            return True
    return False


acg = (Nucleotide.A, Nucleotide.C, Nucleotide.G)
gat = (Nucleotide.G, Nucleotide.A, Nucleotide.T)
print(linear_contains(my_gene, acg))
print(linear_contains(my_gene, gat))

my_sort_gene = sorted(my_gene)
print(binary_contains(my_gene, acg))
print(binary_contains(my_gene, gat))
