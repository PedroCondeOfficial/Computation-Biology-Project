#usr/bin/python3.5
from decimal import * 
import numpy as np
import math

h = 250
dx = 3.54
dy = 2.19
dz = 4.16
d = 4.16
cdist = 254.271392457


file = open("cylinderoutput.pdb","w")

file.write("CRYST1   75.000  75.000  290.000  90.00  90.00  90.00 P 1\n")
mod = 4.16*(math.sin(30))
mod2 = 4.16*(math.sin(60))
seed1 = [340.000,340.000,340.000]
seed2 = [337.920,336.400,340.000]
seed3 = [342.080,336.400,340.000]


rec = "ATOM"
n = 0
atom= "CH4"
name = "CM  "
space = " "*7


while d != h:
    spawn1 = [seed1[0],seed1[1],seed1[2]-dz]
    spawn2 = [seed2[0],seed2[1],seed2[2]-dz]
    spawn3 = [seed3[0],seed3[1],seed3[2]-dz]
    print(spawn1[0])
    kappa = np.linalg.norm(np.array(seed1)-np.array(spawn1))
    if kappa == h:
        break
    elif spawn1[0]<0 or spawn1[1]<0 or spawn1[2]<0 or spawn2[0]<0 or spawn2[1]<0 or spawn2[2]<0 or spawn3[0]<0 or spawn3[1]<0 or spawn3[2]<0:
        break
    else:
        file.write(rec.ljust(6)+str(n).rjust(5)+ " " +  name.ljust(3) + atom +str(n).rjust(6)+space+str(round(spawn1[0],3)).ljust(8)+str(round(spawn1[1],3)).ljust(8)+str(round(spawn1[2],2)).ljust(9)+"\n")
        n += 1
        file.write(rec.ljust(6)+str(n).rjust(5)+ " " +  name.ljust(3) + atom +str(n).rjust(6)+space+str(round(spawn2[0],3)).ljust(8)+str(round(spawn2[1],3)).ljust(8)+str(round(spawn2[2],2)).ljust(9)+"\n")
        n += 1
        file.write(rec.ljust(6)+str(n).rjust(5)+ " " +  name.ljust(3) + atom +str(n).rjust(6)+space+str(round(spawn3[0],3)).ljust(8)+str(round(spawn3[1],3)).ljust(8)+str(round(spawn3[2],2)).ljust(9)+"\n")
        n += 1
        dx += 3.54
        dy += 2.19
        dz += 4.16
        d += 4.16
