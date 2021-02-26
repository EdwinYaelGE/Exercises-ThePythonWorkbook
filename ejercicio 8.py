# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 18:38:32 2021

@author: edwin
"""

print('ejercicio 5\n')
botellasg=float(input('¿Cuantos widgets pediste?  '))
botellasc=float(input('¿Cuantos gizmos pediste ? '))
totalw=botellasg*75
totalg=botellasc*112
peso=totalw+totalg
print('El peso en gramos de tu pedido es:  {0:0.3f}'.format(peso))