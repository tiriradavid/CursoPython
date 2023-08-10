# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 12:11:53 2023

@author: david
"""

# Función Determinar Año Bisiesto
def isYearLeap(year):
    #Cualquier año divisible para 4 es bisiesto
    #Un año divisible para 100 solo es bisiesto si también es divisible para 400
    if (year%4==0 and year%100!=0) or (year%100==0 and year%400==00):
        return True
    else:
        return False

# Función Cuántos días hay en el mes
def daysInMonth(year, month):
    
    # Condición para no ingresar valores menores a 0 o mayores a 12
    if month < 1 or month > 12:
        return None
    
    # Creación Lista con los días en cada mes
    dias_meses = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # Comprobar si es año bisiesto
    # Si es, asignar en mes de febrero un nuevo valor
    if isYearLeap(year)==True:
        dias_meses[2] = 29
        
    return dias_meses[month]

# Función para determinar días en el año
def dayOfYear(year, month, day):
    # Condición para delimitar meses, años y días
    if year < 1 or month < 1 or month > 12 or day < 1 or day > daysInMonth(year, month):
        return None
    
    # Sumatoria de los días hasta el mes que se escribió la fecha
    aux_day = day
    for item in range(1, month):
        aux_day  += daysInMonth(year, item)
    
    return aux_day

# Pruebas
print(dayOfYear(2000, 12, 31))
print(dayOfYear(2023, 1, 31))
print(dayOfYear(2023, 8, 9))
print(dayOfYear(2023, 2, 27))