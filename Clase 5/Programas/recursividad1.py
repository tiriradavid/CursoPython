# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 14:11:25 2023

@author: Juan Carlos
"""
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(5))
print(5*factorial(4))
