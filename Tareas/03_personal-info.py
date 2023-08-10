# -*- coding: utf-8 -*-
"""

@author: david
"""

espacio=" "

#nombre = input("Ingrese su nombre: ")
#apellido = input("Ingrese su apellido: ")
#ubicacion = input("Ingrese su ubicación: ")
edad = int(input("Ingrese su edad: "))

# Con variable "espacio"
#print("Hola mucho gusto, mi nombre es"+espacio+nombre+espacio+apellido+", tengo"+espacio+edad+espacio+"años y vivo en"+espacio+ubicacion+".")

#print("\n")
# Con coma
#print("Hola mucho gusto, mi nombre es",nombre,apellido+", tengo",edad,"años y vivo en",ubicacion+".")

if edad>0 and edad<=10:
    print("Es un infante")
elif edad>10 and edad<=18:
    print("Es un adolescente")
elif edad>18 and edad<=29:
    print("Es un joven adulto")
elif edad>29 and edad<=55:
    print("Es un adulto")
else:
    print("Es una persona de la tercera edad")