# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 18:42:36 2021

@author: edwin
"""

print('ejercicio 9\n')
dinero=float(input('¿Cuanto dinero tiene en su cuenta de ahorros? '))
a1=dinero*1.04
a2=dinero*1.08
a3=dinero*1.12
total= a1+a2+a3
print('El total que ganas en un año por interes es: $ {0:0.2f}'.format(a1))
print('El total que ganas por dos años de interes es: $ {0:1.2f}'.format(a2))
print('El total que ganas por tres años de interes es: $ {0:1.2f}'.format(a3))
print('El total que ganas al final es: $ {0:1.2f}'.format(total))
