# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 12:09:19 2023

@author: Estudiante
"""
import numpy as np
import matplotlib as plt
import scipy as sp

path="C:\\Users\\Estudiante\\Desktop\\"
archivo= "ECGDada.mat"
data= sp.io.loadmat(path+archivo)
print(type(data))
print(data.keys())

ecg= data ["ECGData"]
ecg.shape
ecg= data["ECGData"]["Data"][0][0]
ecg= data["ECGData"][0][0][0]
print(ecg.shape)
print(len(data["ECGData"][0][0]))
plt.plot(ecg[10,0:500])
plt.show()

