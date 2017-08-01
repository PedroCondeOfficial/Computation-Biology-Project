import numpy as np

n = 1
coords = [] 
alt = []
cdist = 117.870425515
fin = []

output = open("output.pdb","w")
output.write("CRYST1  150.000  150.000  150.000  90.00  90.00  90.00 P 1\n")

with open("cylinderoutput.pdb","r") as file:
    for line in file:
        if line.startswith("ATOM"):
            x = float(line[31:37])
            xdist = np.absolute(cdist-x)
            xfin = x - cdist
            y = float(line[39:45])
            ydist = np.absolute(cdist-y)
            yfin = x - cdist
            z = float(line[47:52])
            coords.append([xfin,yfin,z])
            print(xfin,yfin)
n = 1
rec = "ATOM"
n = 1
atom= "CH4"
space = " "*9
           
for items in coords:
    output.write(rec.ljust(6)+str(n).ljust(5)+atom.ljust(5)+str(n).ljust(6)+space+str(round(items[0],3)).ljust(8)+str(round(items[1],3)).ljust(8)+str(round(items[2],3)).ljust(8)+"\n")
    n += 1
