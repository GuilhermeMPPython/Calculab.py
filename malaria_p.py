# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 13:49:11 2019

@author: Guilherme MP
"""

import virgula
import Val
import data

def calculo_Sybr(): #21 linhas
        parasitemia = Val.validFloat(f' Reached parasitemia (%): ')

        parasitemia_desejada = Val.validFloat(f' Desired parasitemia: (%) ')

        diluição_2 = round((parasitemia/parasitemia_desejada),2)

        diluição_1 = 2.5

        fator_diluição = round((diluição_1 * diluição_2),2)

        hemacias_infectadas = round((18000/fator_diluição),2)
        (f'''
 Reached/desired parasitemia = dilution 2

{parasitemia}/{parasitemia_desejada} =  dilution 2


dilution 2 = {diluição_2}

 dilution factor = {diluição_2} x 2,5

 dilution factor = {fator_diluição}

 infected RBC's = 18000/fat. diluição

 infected RBC's = 18000/{fator_diluição}

 infected RBC's = {hemacias_infectadas} µL
''')

        print(f' -> Dilution factor: {fator_diluição}')
        print()
        print(f" -> infected RBC's: {hemacias_infectadas} µL")
        print()
        print(f" -> Fresh RBC's: 720 µL")
        print()
        print (' Date:',data.data())

def hemacias(): #10 linhas
        n = Val.validInt(f" How many RBC's in the quadrant? ")
        campo = n*4
        n_campos = 1000/campo
        print()
        print(f'''
Nº of fields = 1000/(Number of RBCs counted x 4)

Nº of fields = 1000/{n} x 4

Nº of fields = 1000/{campo}

Nº of fields = {round(n_campos,2)}

''')
        print(' Date:',data.data())

        

def in_vivo(): #38 linhas
        print()
        num_camundongos = Val.validInt(f' Nº of mice to be infected: ')
        parasitemia = Val.validFloat(f' Parasitemia (%): ')
        num_hemacias = Val.validInt(f' RBCs counted: ')
        potencia = 'x 10^6'
        hemacias_totais = round((num_hemacias/20),3)
        hemacias_parasitadas = round((hemacias_totais*(parasitemia/100)),3)
        hemacias200µL = round((hemacias_parasitadas/5),2)
        V1 = round((200/hemacias200µL),3)

        if V1*(num_camundongos+3) <1000:
                hem_total = (V1)*(num_camundongos+3)
                unit_hem = 'µL'
        elif V1*(num_camundongos+3) >=1000:
                hem_total = (V1)*(num_camundongos+3)/1000
                unit_hem = 'mL'
        
        if (200-V1)*(num_camundongos+3) <1000:
                meio_total = (200-V1)*(num_camundongos+3)
                unit_meio = 'µL'
        elif (200-V1)*(num_camundongos+3) >=1000:
                meio_total = (200-V1)*(num_camundongos+3)/1000
                unit_meio = 'mL'
        print()
        print(f' Total Nº of infected RBCs: {round(hemacias_parasitadas,2)} {potencia}')
        print(f' In 200 µL there are {round(hemacias200µL,2)} {potencia} parasitized RBCs')
        print()
        print(f''' 200 µL ------------------- {round(hemacias200µL,2)} x 10^6
        
 V1  ---------------------- 1x10^6


 200 x 10^6 = {hemacias200µL} x 10^6 x V1

 V1 = 200/{hemacias200µL}

 V1 = {V1} µL''')
        print()
        print(f''' > Volume required to obtain
   1x10^6 infected RBCs: {round(V1,2)} µL''')
        print()
        print(f''' > Volume of medium
   to complete 200 µL: {round((200-V1),2)} µL''')
        print()
        print(f' > RBCs p/ {num_camundongos+3} mice: {round(hem_total,3)} {unit_hem}')
        print(f' > Total volume of medium: {round(meio_total,3)} {unit_meio}')
        print()
        print (' Date:',data.data())


def calculo_gametocitos(): #39 linhas
        hematocrito = 6

        meio = Val.validFloat(f' Volume of medium (mL): ')

        x = round((meio/100),2) *6

        parasitemia_obtida = Val.validFloat(f' Obtained parasitemia (%): ')

        parasitemia_desejada = Val.validFloat(f' Desired parasitemia (%): ')

        razão = parasitemia_obtida/parasitemia_desejada

        hemacias_infectadas = round((x/razão),3)
        if hemacias_infectadas >= 1:
                hemacias_infectadas1  = hemacias_infectadas
                unit1 = 'mL'
        elif hemacias_infectadas < 1:
                hemacias_infectadas1  = hemacias_infectadas*1000
                unit1 = 'µL'
      
        hemacias_novas = round(((x - hemacias_infectadas)*2),3)
        if hemacias_novas >= 1:
                hemacias_novas1  = hemacias_novas
                unit2 = 'mL'
        elif hemacias_novas < 1:
                hemacias_novas1  = hemacias_novas*1000
                unit2 = 'µL'
        
        if hemacias_novas <= 0:
                print()
                print(f' -> There is no way to add new RBCs')
                print()
        else:

                print(f'''
 ***Hematocrit***

 6 ------ 100 mL
 X -------- {meio} mL

 100X = {meio*6}

 X = {round(x,3)} mL


 ***Dilution of the parasitemia***

 Reached/desired parasitemia -> {round(razão,2)}

 {round(x,2)}/{razão} = {round(hemacias_infectadas,2)} mL


 ***Fresh and infected RBCs***

 ({round(x,2)} - {round(hemacias_infectadas,2)}) x 2 = {round(hemacias_novas,2)} mL

''')
                
                print(f' -> Infected RBCs: {hemacias_infectadas1} {unit1}')
                print()
                print(f' -> Fresh RBCs: {hemacias_novas1} {unit2}')
                print()
                print (' Date:',data.data())