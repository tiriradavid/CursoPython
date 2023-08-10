# -*- coding: utf-8 -*-
"""

@author: david
"""

#Iniación
tupla=()
lista=[]

tupla=(4, 78.9, "R1", True)
lista=[4, 78.9, "R1", True]

print(tupla)
print(lista)

print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])

print(lista[-1])

print("\n")
aux=lista[0]
aux1=lista[1]
print(aux1)

print("\n")
lista[3]="AP1"
print(lista[3])

del lista[2]
print(lista[2])
