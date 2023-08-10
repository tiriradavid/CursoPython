# -*- coding: utf-8 -*-
"""

@author: david
"""

espacio=" "

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
ubicacion = input("Ingrese su ubicación: ")
edad = input("Ingrese su edad: ")

# Con variable "espacio"
print("Hola mucho gusto, mi nombre es"+espacio+nombre+espacio+apellido+", tengo"+espacio+edad+espacio+"años y vivo en"+espacio+ubicacion+".")

print("\n")
# Con coma
print("Hola mucho gusto, mi nombre es",nombre,apellido+", tengo",edad,"años y vivo en",ubicacion+".")