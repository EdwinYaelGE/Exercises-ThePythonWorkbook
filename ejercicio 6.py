# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 18:19:30 2021

@author: edwin
"""

print('ejercicio 6\n')
preciocomida=float(input('¿Cual fue el costo de su ticket? '))
iva=preciocomida*.16
propina=preciocomida*.18
total= preciocomida+iva+propina
print('El total que debes de pagar de impuesto es: $ {0:0.3f}'.format(iva))
print('El total que debes de pagar de propina es: $ {0:1.3f}'.format(propina))
print('El total que debes de pagar de tu comida es: $ {0:1.3f}'.format(total))
