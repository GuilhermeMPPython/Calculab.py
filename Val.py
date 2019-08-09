# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 13:54:47 2019

@author: Guilherme MP
"""

print ()
def validInt(a):
    while True:
        try:
            n = int(input (f'{a}'))
            print()
        except(ValueError):
            print(' Invalid input: type an integer number')
            print ()
        else:
            break
    return n

def validFloat(b):
    while True:
        try:
            n = float(input (f'{b}'))
            print()
        except(ValueError):
            print(' Invalid input: type a number')
            print ()
        else:
            break
    return n
    
def validStr(c):
    while True:
        try:
            n = float(input (f'{c}'))
            print()
        except(ValueError):
            print(' Invalid input: type a string')
            print ()
        else:
            break
    return n