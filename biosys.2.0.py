import matplotlib.pyplot as plt
import numpy as np
from numpy.lib.function_base import average

def delta(BestValue,Sensitiveness,EnviValue):
    return 8*(Sensitiveness**(BestValue-EnviValue))/((Sensitiveness**(BestValue-EnviValue))+1)**2-1

def GetEnvi():    
    global Envi
    Envi=['sun:','O2:','CO2:','water:','salt:','stability:']
    for i in range(0,len(Envi)):
        Envi[i]=eval(input(Envi[i]))
GetEnvi()   
a=np.array([[2,2],[2,4],[2,5],[2,1.2],[3,10]])
def CalcChange():
    change=['sun:','O2:','CO2:','water:','salt:']
    for i in range(0,len(Envi)-1):
        change[i]=delta(a[i][0],a[i][1],Envi[i])
        Envi[i]=Envi[1]-(1-Envi[5])*change[i]
    return average(change)
print(CalcChange(),'\n',Envi,'\n\n')
print(CalcChange(),'\n',Envi)