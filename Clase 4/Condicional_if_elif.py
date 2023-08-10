# -*- coding: utf-8 -*-
"""
@author: david
"""

acl=int(input("Ingrese el # número de ACL: "))

if acl>=1 and acl<=99:
    print("Es una ACL estandar")
elif acl>=100 and acl<=199:
    print("Es una ACL extendida")
else:
    print("El número ingresado no es una ACL")
    
