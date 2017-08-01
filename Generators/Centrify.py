import numpy as np
import random
import decimal

n = 0
coords = [] 
alt = []
xdist = 315
ydist = 315
zdist = 280


fin = []



output = open("output.pdb","w")
output.write("CRYST1   45.000  45.000  75.000  90.00  90.00  90.00 P 1\n")

with open("final.pdb","r") as file:
    for line in file:
        if line.startswith("ATOM"):
            x = float(line[31:37])
            xfin = x - xdist
            xl = str(round(decimal.Decimal(str(xfin) + '0' * 3),3))
            y = float(line[39:45])
            yfin = y - ydist
            yl = str(round(decimal.Decimal(str(yfin) + '0' * 3),3))
            z = float(line[47:52])
            zfin = z - zdist
            zl = str(round(decimal.Decimal(str(zfin) + '0' * 3),3))
            coords.append([xl,yl,zl])
            atomnum = float(line[9:11])
   
            
rec = "ATOM"
n = 0
atom= "CH4"
name = "CM  "
space = " "*6

for items in coords:
        output.write(rec.ljust(6)+str(n).rjust(5) + " " +  name.ljust(3) + atom + "  " + str(n).rjust(4)+space+str(items[0]).ljust(8)+str(items[1]).ljust(6)+str(items[2]).rjust(8)+"\n")
        n += 1
