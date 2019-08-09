# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 13:53:57 2019

@author: Guilherme MP
"""

import virgula
import Val
import data

def combinação(): #15 linhas
    print (' ',data.data())  
    t = int(input(f'''
[1] Cálculo concentral inicial: poço 1A
[2] Cálculo do FIC

'''))
    if t == 1:
        C1 = float(input(f' Qual a concentração da solução estoque? '))
        print(f' A quantidade a ser retirada é de ')
    if t == 2:
        IC50AC = float(input(f' IC50 da droga A em combinação? '))
        IC50A = float(input(f' IC50 da droga A sozinha? '))
        IC50BC = float(input(f' IC50 da droga B em combinação? '))
        IC50B = float(input(f' IC50 da droga B sozinha? '))
        ΣFIC = (IC50AC/IC50A) + (IC50BC/IC50B)
        print(f''' 
ΣFIC = (IC50AC/IC50A) + (IC50BC/IC50B)
ΣFIC = ({IC50AC}/{IC50A}) + ({IC50BC}/{IC50B})
ΣFIC = ({round((IC50AC/IC50A),2)}) + ({round((IC50BC/IC50B),2)})
ΣFIC = {round(ΣFIC,2)}''')
                
        print()
        print(f'>>> O ΣFIC resultante é de {virgula.virgula(round(ΣFIC,2))}')

        
def molaridade(): #35 linhas
    data.data()
    lista = [[]]
    i = 0
    while True:
        nome = str(input(f'Qual o nome da droga? '))
        lista[i].append(nome)
        PM  = float(input(f'Peso molecular: '))
        conc = float(input(f'Concentração(sem unidade):  '))
        MW = round(((conc/PM)*1000),2)
        lista[i].append(MW)
                
        opção = int(input(f'''Unidade:

[1] mM
[2] µM
[3] nM
[4] pM

'''))
        if opção == 1:
            concentração = 'mM'        
        if opção == 2:
            concentração = 'µM'
        if opção == 3:
            concentração = 'nM'
        if opção == 4:
            concentração = 'pM'
                        
        lista[i].append(concentração)
        lista.append([])
        i += 1
        print()
        resp = str(input(f'Mais uma droga? [S/N] '))
        if resp in 'nN':
            print()
            lista.remove(lista[len(lista)-1])
            break
        for p in lista:
                print(f'{p[0]}: {p[1]} {p[2]}')
                print()

        print()

def diluicao_droga(): #11 linhas
        C1 = float(input(f' Conc. da solução estoque (µM): '))

        C2 = float(input(f' Conc. da solução desejada (µM): '))

        V2 = float(input(f' Volume de diluição (µL):'))
        print()

        V1 = round(((C2 * V2)/C1),2)

        volume_de_meio = V2 - V1
        print()
        print (' ',data.data())
        print ()
        print(f''' =============================
C1V1 = C2V2

{C1} x V1 = {C2} x {V2}
V1 = {C2} x {V2}/{C1}
V1 = {round((C2*V2/C1),2)} 
=============================''')
        print()

        print(f' Volume de droga = {virgula.virgula(V1)} µL')
        print()
        print(f' Volume de meio = {virgula.virgula(volume_de_meio)} µL')
        print()


def calculo_drogas(): #8 linhas
        n = int(input(f'''[1] Diluição
[2] Molaridade

'''))
        if n == 1:
                diluicao_droga()
        if n == 2:
                molaridade()