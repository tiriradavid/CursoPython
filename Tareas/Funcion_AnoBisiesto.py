# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 12:11:53 2023

@author: david
"""

def isYearLeap(year):
    #Cualquier año divisible para 4 es bisiesto
    #Un año divisible para 100 solo es bisiesto si también es divisible para 400
    if (year%4==0 and year%100!=0) or (year%100==0 and year%400==00):
        return True
    else:
        return False

def daysInMonth(year, month):
    if month < 1 or month > 12:
        return None
    
    dias_meses = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if isYearLeap(year)==True:
        dias_meses[2] = 29
    
    return dias_meses[month]


#Pruebas
print(daysInMonth(1900,2))
print(daysInMonth(2000,2))
print(daysInMonth(2016,1))
print(daysInMonth(1987,11))


testYears = [1900, 2000, 2016, 1987]

testMonths = [2, 2, 1, 11]

testResults = [28, 29, 31, 30]

for i in range(len(testYears)):

              yr = testYears[i]

              mo = testMonths[i]

              print(yr, mo, "->", end="")

              result = daysInMonth(yr, mo)

              if result == testResults[i]:

                            print("OK")

              else:

                            print("Failed")