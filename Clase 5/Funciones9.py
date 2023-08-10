# -*- coding: utf-8 -*-
"""

@author: david
"""

# lista como resultado de una función
def crearLista(n):
    lista=[]
    for item in range(n):
        lista.append(item)
    return lista
print(crearLista(5))
a=crearLista(7)
print(a)