# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 13:51:19 2019

@author: Guilherme MP
"""
import virgula
import Val
import data
    
def leishmania():   
    spc = ['','Leishmania amazonensis','Leishmania infantum','Leishmania braziliensis']
    while True:
        esp = Val.validInt(f''' Species:
[1]L. amazonensis 
[2]L. infantum
[3]L. braziliensis
[4]Other species

''')
        if esp == 1 or esp == 2 or esp == 3 or esp == 4:
            if esp == 4:
                espe = str(input (f' Species: '))
                spc.append(espe)
            break
        
    pas = Val.validInt(f' Passage: ')
    
    while True:
        perg = str(input (f'''
Standardize [Y/N]? '''))
        if perg in "yY":        
            while True:
                print()
                perg1 = str(input (f' Change potency [Y/N]? '))
                if perg1 in "yY":
                    while True:
                        pot = int(input(f''' Which potency?
[1] 10^4
[2] 10^5
[3] 10^7
[4] 10^8

'''))
                        if pot ==1:
                            t = 4
                            potencia = 10000
                            break
                        if pot ==2:
                            t = 5
                            potencia = 100000
                            break
                        if pot ==3:
                            t = 7
                            potencia = 10000000
                            break
                        if pot ==4:
                            t = 8
                            potencia = 100000000
                            break
                    print()
                    break          
                if perg1 in "nN":
                    t = 6
                    potencia = 1000000
                    print()
                    break
        
            while True:
                perg2 = str(input(f' Change the unit of 10^ {t} [Y/N]? '))
                if perg2 in "yY":
                    unit1 = Val.validFloat(f' New unit: ')
                    break
                elif perg2 in "nN":
                    unit1 = 1
                    break
                print()
        
            while True:
                perg3 = str(input (f' Change the volume of 1000 µL [Y/N] ? '))
                if perg3 in "yY":
                    vol1 = Val.validInt(f' New volume: ')
                    break
                if perg3 in "nN":
                    vol1 = 1000
                    break
                print()
            break
        if perg in "nN":
            potencia = 1000000
            t = 6
            unit1 = 1
            vol1 = 1000
            break
    print(f''' 
Potency: {potencia}
Unit: {unit1} x 10^{t}
Volume: {vol1} µL
''')

    while True:
        exp = Val.validInt(f''' [1] IC50 \t [2] Infection
 ''')
        if exp == 1:
            z = 30
            break
        elif exp == 2:
            z = 200
            break

    n = Val.validInt(f' Leishmanias counted: ')
    fatd = Val.validInt(f' Dilution factor: ')

    total = n*fatd*10000

    x = (unit1*potencia)*vol1/total

    x1 = round(x,2)

    y = round((z-x),2)

    nplacas = int(vol1//(x*100))
    npocos = nplacas*100
    
    hpocos = int(vol1//x)

    if x*npocos >= 1000:
        xpocos = (x*npocos)/1000
        unitx = 'mL'
    else:
        xpocos = x*npocos
        unitx = 'µL'
    
    if y*npocos >= 1000:
        ypocos = (y*npocos)/1000
        unity = 'mL'
    else:
        ypocos = y*npocos
        unity = 'µL'
        
    print(f'''
 {n} x {fatd} x 10^4 = {total} x 10^4

 {total/(10**6)} x 10^6 --------------- 1000

 {unit1} x 10^{t}  ------------------- X

 {unit1} x 10^{t+3}/{total/(10**4)} x 10^4 = X

 X = {round(x,2)} µL''')

    if nplacas < 1:
        print()
        print(f' > É possível fazer apenas {int(1000//x)} poços')
    else:
        if nplacas == 1:
            placa = 'plate'
        
        elif nplacas > 1:
            placa = 'plates'                         
        print()
        print(f' Species: {spc[esp]}')
        print(f' Passage: {pas}°')
        print()
        print(f' -> It is possible to fill {nplacas} {placa}/{hpocos} wells')
        print()
        print(f' -> Leishmania/well : {x1} µL')
        print(f' -> Medium/well {y} µL')
        print()
        qua = Val.validInt(f' How many wells do you want to fill? ')
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

        print(f' -> Leishmanias/{qua} wells: {round(xpocos,2)} {unitx}')
        print(f' -> Medium/ {qua} wells: {round(ypocos,3)} {unity}') 
        print()
        print (' Data:',data.data())
        print ()
        return x1
           
         
def leishmania_in_vivo():
    import virgula
    while True:
        opc = int(input (f''' [1] Promastigote counting
[2] Dose calculation for mice

  '''))
        if opc == 1:        
            spc = ['','amazonensis','infantum','braziliensis']
            import virgula #32 linhas
            esp = int(input(f''' Species:
[1]L. amazonensis 
[2]L. infantum
[3]L. braziliensis
'''))

            if esp == 1 or esp == 3:
                vol_tot = 30
            elif esp == 2:
                vol_tot = 500
        
            passagem = int(input(f' Passage: '))    
            n = int(input(f' Leishmania counted: '))
            fat_dil = int(input(f' Dilution factor: '))
            n_cam = int(input(f' Nº of mice to be infected: '))
            total = n*fat_dil*(10**4)
            quant_leish = (10**9)/(n*fat_dil*10**4)
            pbs = vol_tot - quant_leish
            unit = 'µL'
            quant_leish_cam = n_cam * quant_leish
            quant_pbs_cam = n_cam * pbs
            unit_tot_meio = 'µL'
            if quant_pbs_cam < 1000:
                unit_tot_meio = 'µL'
            elif quant_pbs_cam >= 1000:
                unit_tot_meio = 'mL'
            print(f'''
 {n} x {fat_dil} x 10^4 = {total} x 10^4

 {total/(10**6)} x 10^6 --------------- 1000

 1 x 10^7  ------------------- X

 10^10/{total/(10**4)} x 10^4 = X

 X = {round(quant_leish,2)} µL''')
        
            print()
            print(f' Species: Leishmania {spc[esp]}')
            print(f' Passage: {passagem}ª')
            print()
            print(f' > Volume of leishmania: {virgula.virgula(round(quant_leish,2))} {unit}')
            print()
            print(f' > Volume of PBS: {virgula.virgula(round(pbs,2))} {unit}')
            print()
            print(f' > Vol. Leish/{n_cam} mice: {virgula.virgula(round(quant_leish_cam,2))} {unit}')
            print(f' > Vol. PBS/{n_cam} mice: {virgula.virgula(round(quant_pbs_cam,2))} {unit_tot_meio}')
            break

        elif opc == 2:            
            print()
            dose = float(input (f' Desired dose (mg/kg): '))
            subst = dose*1000 #quant em mcg

            conc = float(input (f' Conc. mother solution (µg/mL): '))

            print()

            print (f''' {subst}  µg ------------ 1000g

 vol. withdrawn -------- peso

 vol. withdrawn x 1000 = {subst} x weight

 vol. withdrawn = ({subst} x peso)/1000

 -> vol. withdrawn = {subst/1000} x peso''')
            print()

            peso = float(input(f' Weight (g): '))

            Y = ((dose*peso)*1000)/(conc)

            print (f'''
 {conc} µg ----------- 1000 µg

 {dose* peso} µg -------------- Y

 {conc} x Y = {dose* peso}*1000

 Y = {round (Y,2)} µL
  
''')
            if Y > 500:
                print(f''' -> The volume of substance to be withdrawn
is higher than the inoculum volume (500µL)''')
                print()
                break
            else:                               
                print()
                print(f' -> vol. withdrawn: {virgula.virgula(round(Y,2))} µL')
                print(f' -> Vol. vehicle to complete: {virgula.virgula(round((500-Y),2))} µL') 
                print ()
                print(' Date:',data.data())
                break
