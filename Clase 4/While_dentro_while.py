# -*- coding: utf-8 -*-
"""

@author: david
"""

while True:
    x=input("Ingresar un número a contar: ")
    if x== 'q' or x=='quit':
        break

    x=int(x)
    y=1
    while True:
        print(y)
        y=y+1
        if y>x:
            break