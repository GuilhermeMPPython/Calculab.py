# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 13:52:39 2019

@author: Guilherme MP
"""

print()
import data
import Val
#Conta celula
def celula():
    cels = ['','HepG2','VERO','J774','THP-1']
    import virgula
    z = 180
    while True:
        lin = Val.validInt(f''' Cell line: 
[1] HepG2 \t [2] VERO
[3] J774 \t [4] THP-1

 ''')

        if lin == 1 or lin == 2 or lin == 3 or lin == 4:
            break
    if lin == 1 or lin == 2 or lin == 3:
        fat = 10000
        fat1 = '10^4'
        fat2 = '10^7'
        quant = 1
    elif lin == 4:
        fat = 100000
        fat1 = '10^5'
        fat2 = '10^8'
        while True:
            perg = Val.validInt(f''' [1] CC50\t[2] Infection
[3] Split        
''')
            if perg == 1:
                quant = 1
                z = 180
                break
            elif perg == 2:
                quant = 2.5
                z = 200
                break
            elif perg == 3:
                V2 = Val.validInt(f' Final volume: ')
                valor = Val.validInt(f'Unit that precedes 10^5: ')
                C2 = valor*100000
                

    n = Val.validInt(f' Cells counted: ')
    fatd = Val.validInt(f' Dilution factor: ')

    total = (n/4)*fatd*10000

    x = (1000*fat*quant)/total

    x1 = round(x,2)

    y = round((z-x),2)

    nplacas = int(1000//(x*96))
    npocos = int(1000//x)
    
    if nplacas < 1:
        placa = 'plate'

    if nplacas == 1:
        placa = 'plate' 
        
    elif nplacas > 1:
        placa = 'plates'
        
    print()
    print(f' Cell line: {cels[lin]}')
    print ()
    print(f'''
 {n}/4 x {fatd} x 10^4 = {total} x 10^4

 {total/(10**6)} x 10^6 --------------- 1000

 {quant} x {fat1}  ------------------- X

 {fat2}/{total/(10**4)} x 10^4 = X

 X = {round(x,2)} µL''')

    print()
    print(f' -> It is possible to fill {npocos} wells/{nplacas} {placa}')
    print()
    print(f' -> Cells/well: {x1} µL')
    print(f' -> Medium/well: {y} µL')
    print()
    qua = Val.validInt(f' How many wells do you like to fill? ')
    print()
    if x*qua >= 1000:
        xpocos = (x*qua)/1000
        unitx = 'mL'
    else:
        xpocos = x*qua
        unitx = 'µL'
    
    if y*qua >= 1000:
        ypocos = (y*qua)/1000
        unity = 'mL'
    else:
        ypocos = y*qua
        unity = 'µL'

    print(f' -> Volume of cells for {qua} wells: {round(xpocos,2)} {unitx}')
    print(f' -> Volume of medium for {qua} wells: {round(ypocos,3)} {unity}')
    print()
    print (' Date:',data.data())
    return x1