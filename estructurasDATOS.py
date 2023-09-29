# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 09:24:29 2023

@author: Estudiante
"""

#a=np.zeros(10)
#lista1=[0,15,8,9,7,5,4,7,8,2]
#lista2=[2,15,28,29,97,15,14,27,78,82]
#b=np.array((lista1, lista2,a))
#print(b)
#print(b[1][2])
#print(b[:,1:3])




#      L I S T A S 
#crear lista
#my_list= [4, 50, "hola", True, 4.8, [3, 6,[7, 4, True, 8.9], 8, 0.8], 19, 20, 58, 9, 33]
#print(my_list[5])
#print(my_list[4])

#print(my_list[2])
#print(my_list[5][2][2])
#print(my_list[:-1])
#print(my_list[1:])
#print(my_list[1:7])
#print(my_list[1:10:2])  # INICIO, FIN, PASOS

#my_list[len(my_list):]=[789]
#my_list.append(555)
#name=input("Ingrese su name:   ")
#my_list.append(name)
#my_list
#my_list.insert(2, "JJJ")
#print(my_list)

#for i in my_list:
#    print(i)




# import numpy as np
# new_list=[]
# datos = np.random.randint(0,101,100)
# print(datos)
# for i in datos:
#     if i > 90:
#         new_list.append(i)
# print(new_list)
# len(new_list)


lista1= [45,89,23,73,2,8,27,10,405,156,256]

def funLIST(ext_list):
    otraL=[]
    for i in range(len(lista1)-1):
        z=lista1[i+1]- lista1[i]
        otraL.append(z)
    return otraL

print(funLIST(lista1))


#  M A T R I C E S       D E      L I S T A S
# I M P R I M I R      M A T R I C E S :
matrix=[[35, 7, 2], [1, 9, 3], [5, 8, 95]]
print(matrix)

for i in matrix:
    for j in i:
        print(j, "\t ", end="")   #end para no hacer salto de linea
    print()
print(matrix[1][1:])


xx= [i for i in range(2,51,2)]
print(xx)



