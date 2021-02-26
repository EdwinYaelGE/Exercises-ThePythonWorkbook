# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 18:09:38 2021

@author: edwin
"""

print('ejercicio 4\n')
ancho=float(input('ingresa el ancho de la granja en pies: '))
largo=float(input('ingresa el largo de la granja en pies: '))
area=ancho*largo
areaconvertida=area*43560
print('El area de tu habitacion es: {0:0.3f} en acres'.format(areaconvertida))