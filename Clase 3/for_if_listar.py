# -*- coding: utf-8 -*-
"""

@author: david
"""

listar1=[]
listar2=[]
listar3=[]
listar4=[]

lista=["R1", "R2", "R3",
       "S1","S2","S3",
       "AP1","AP2","AP3",
       "FW2","PC1","PC2"]

for item in lista:
    if "R" in item:
        listar1.append(item)
    elif "S" in item:
        listar2.append(item)
    elif "AP" in item:
        listar3.append(item)
    else:
        listar4.append(item)

print(listar1)
print(listar2)
print(listar3)
print(listar4)