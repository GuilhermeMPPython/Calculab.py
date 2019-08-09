# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 13:57:53 2019

@author: Guilherme MP
"""
import datetime
def data():
    hoje = datetime.date.today()
    if hoje.day < 10:
        dia = '0'+str(hoje.day)
    else:
        dia = str(hoje.day)
    if hoje.month < 10:
        mes = '0'+str(hoje.month)
    else:
        mes = str(hoje.month)
    formatada = dia + '/' + mes + '/' + str(hoje.year)
    return formatada