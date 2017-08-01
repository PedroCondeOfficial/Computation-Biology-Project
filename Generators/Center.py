import numpy as np 

c = []

with open("final.pdb","r") as file:
    for line in file: 
        if line.startswith("ATOM"):
            x = float(line[31:37])
            y = float(line[39:45])
            z = float(line[47:52])
            c.append(np.array([x,y,z]))
            
xi = np.mean(c[0])
ypsilon = np.mean(c[1])
zeta = np.mean(c[2])
center = [xi,ypsilon,zeta]
print(center)
c = [137.92,136.4,69.28]
boxcent = [35,35,145]
d = np.linalg.norm(np.array(c[0])-np.array(boxcent[0]))
d2 = np.linalg.norm(np.array(c[1])-np.array(boxcent[1]))
d3 = np.linalg.norm(np.array(c[2])-np.array(boxcent[2]))
print(d)
print(d2)
print(d3)

            