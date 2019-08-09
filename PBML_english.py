# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 13:44:08 2019

@author: Guilherme MP
"""

import celula_p
import leishmania_p
import malaria_p
import moleculas_p
import Ensaio_RAW
import Val

while True:
    print()
    n = Val.validInt(f''' Choose the operation:
[1] Cells           \t\t\t[2] Leishmania
[3] Sybr            \t\t\t[4] Erythrocytes
[5] P. berghei       \t\t\t[6] Gametocytes
[7] Drug interaction\t\t\t[8] Drug conc. calculus
[9] Leishmania       \t\t\t[10] RAW infection assay 
in vivo


''')

    if n == 1:
        celula_p.celula()
        print()
        resp = str(input (f'Continue [Y/N]? '))
        if resp in 'nN':
            break
    if n == 2:
        leishmania_p.leishmania ()
        print()
        resp = str(input (f'Continue [Y/N]? '))
        if resp in 'nN':
            break
    if n == 3:
        malaria_p.calculo_Sybr()
        print()
        resp = str(input (f'Continue [Y/N]? '))
        if resp in 'nN':
            break
    if n == 4:
        malaria_p.hemacias()
        print()
        resp = str(input (f'Continue [Y/N] ? '))
        if resp in 'nN':
            break
    if n == 5:
        malaria_p.in_vivo()
        print()
        resp = str(input (f'Continue [Y/N]? '))
        if resp in 'nN':
            break
    if n == 6:
        malaria_p.calculo_gametocitos()
        print()
        resp = str(input (f'Continue [Y/N]? '))
        if resp in 'nN':
            break
    if n == 7:
        moleculas_p.combinação()
        print()
        resp = str(input (f'Continue [Y/N]? '))
        if resp in 'nN':
            break
    if n == 8:
        moleculas_p.diluicao_droga ()
        print()
        resp = str(input (f'Continue [Y/N]? '))
        if resp in 'nN':
            break
    if n == 9:
        leishmania_p.leishmania_in_vivo()
        print()
        resp = str(input (f'Continue [Y/N]? '))
        if resp in 'nN':
            break
    if n == 10:
        Ensaio_RAW.ensaio_infeccao_RAW()
        print()
        resp = str(input (f'Continue [Y/N]? '))
        if resp in 'nN':
            break
            
    print (f'''
!!!''')
