# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 09:36:40 2021

@author: edwin
"""
from math import acos,sin,cos,radians

print('ejercicio 12')

t1=float(input('ingerese el valor de T1: '))
g1=float(input('ingerese el valor de G1: '))
t2=float(input('ingerese el valor de T2: '))
g2=float(input('ingerese el valor de G2: '))
distancia= (6371.01)*(acos((sin(radians(t1)))*(sin(radians(t2))*(cos(radians(g1)-radians(g2))))))
print('la distancia entre 2 punto es: {0:0.3f}'.format(distancia)+' KM')