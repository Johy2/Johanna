# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 11:07:51 2023

@author: Estudiante
"""
# D I C C I O N A R I O S:
mydict={'name':['Elena', "Juan", "Pedro"], 
        "edades":[25,20,35], 
        "matrix": [[3,1,5],[7,2,6]]}

mydict2= dict(name=[2,5,6])
print(mydict["edades"][1])
print(mydict["matrix"][1][:-1])

#métodos de diccionarios
mydict.keys()
mydict.values()
mydict.items()
for i in mydict.values():
    print(i)
for i in mydict.keys():
    print(i)
for i in mydict.items():
    print(i)
    



