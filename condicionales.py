# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 12:21:08 2023

@author: Estudiante
"""

#" IF    ELSE "

datos=1
nativa=100
if datos== nativa:
    print("Las variables son iguales")
else: 
    print("Las variables no son iguales")
    
    
    
 #" ELIF "
   
acl=int(input("Ingrese un valor:  "))
if acl>=1 and acl <=99:
    print("Es un ACL estandar")
elif acl>=100 and acl<=199:
    print("Es un ACL extendido")
else:
    print("El valor ingresado no es un ACL")
    
    
#" EJERCICIO "
edad= int(input("Ingrese una edad:  "))
if edad<0:
    print("AUN NO EXISTE")
elif edad>=0 and edad <=2:
    print("BEBÉ")
elif edad>=3 and edad<=11:
    print("PUBERTAD")
elif edad>=12 and edad <=17:
    print("ADOLESCENTE")
elif edad>=18 and edad  <=59:
    print("ADULTO/A")
elif edad >=60 and edad<=64:
    print("TERCERA EDAD")
else:
    print("VIEJITO/A")
    
    
    
#    " FOR "

listaR=[]
listaS=[]
listaV=[]
lista=["R1", "R2", "R3", "R4", 
       "S1", "S2", "S3", "S4", "S5",
       "AP2", "AP3", "AP4","OLT1","IoT1", "IoT2"]
print(lista[0])
for item in lista:
   if "R" in item:
       listaR.append(item)
       
   elif "S" in item:
           listaS.append(item)
           
   else:
           listaV.append(item)
                
print(listaR) 
print(listaS) 
print(listaV)         