# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 13:55:44 2019

@author: Guilherme MP
"""

import celula_p
import leishmania_p
import virgula

def ensaio_infeccao_RAW():
    print (' ','='*38)
    print('\t CÁLCULO LEISHMANIA')
    print(' ','='*38)
    leish_poco = round(leishmania_p.leishmania(),2)
    print (' ','='*38)
    print('\tCÁLCULO CÉLULAS RAW')
    print(' ','='*38)
    cel_poco = round (celula_p.celula(),2)
    quant_meio = 180 - (leish_poco + cel_poco)
    print()
    print (' ','='*38)
    print('\tENSAIO DE INFECÇÃO RAW')
    print(' ','='*38)
    p = int(input(f''' 
N° de poços: '''))
    print(f' -> Quant de leish + cel/poço: {virgula.virgula(round((leish_poco + cel_poco),2))} uL')
    print (f' -> Total de leishmania: {virgula.virgula(leish_poco*4)} uL')
    print (f' -> Total de celula: {virgula.virgula(cel_poco*4)} uL')
    print (f' -> Total de meio: {virgula.virgula(quant_meio*4)} uL')