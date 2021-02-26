# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 18:13:32 2021

@author: edwin
"""

print('ejercicio 5\n')
botellasg=float(input('¿Cuantas botellas de mas de un litro tienes?  '))
botellasc=float(input('¿Cuantas botellas de menos de un litro tienes? '))
totalg=botellasg*0.25
totalc=botellasc*0.10
rembolso=totalg+totalc
print('El total que te deben rembolsar es: $ {0:0.3f}'.format(rembolso))