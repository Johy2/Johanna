# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 14:47:06 2023

@author: Estudiante
"""

contar=int(input("Ingrese un número a contar:   "))
contador =2
while contador <= contar:
    print(contador)
    contador+=2
    
    #break::::::
    
x=int(input("Ingrese un número a contar:   "))
y =1
while True:
    print(y)
    y=y+1
    if y>x:
        break
    
    
    
    
while True:
    x= input("Enter a number to count to:  ")
    if x== 'q' or x=='quit':
        break
    x=int(x)
    y=1
    while True:
        print(y)
        y=y+1
        if y>x:
            break
    
    