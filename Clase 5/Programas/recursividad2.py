# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 14:26:12 2023

@author: Juan Carlos
"""

def sum_digits(n):
    if n < 10:
        return n
    else:
        return n % 10 + sum_digits(n // 10)
print(sum_digits(12345))