import numpy as np

n = open("final.pdb","w")
n.write("CRYST1   75.000  75.000  290.000  90.00  90.00  90.00 P 1\n")


with open("cylinderoutput.pdb", "r") as file:
    for line in file: 
        if line.startswith("ATOM"):
            x = float(line[31:37])
            y = float(line[39:45])
            z = float(line[47:52])
            atom = [x,y,z]
            seed1 = [340.000,340.000,340.000]
            dist = np.linalg.norm(np.array(seed1)-np.array(atom))
            h = 46
            if dist < h:
                n.write(str(line))
                
