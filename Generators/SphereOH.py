import math
import random
import decimal

with open("sp.pdb", "r") as file: 
    n = 73
    atom = "CH4"
    atom1 = "O"
    atom2 = "H"
    rec = "ATOM"
    f = open("sOH.pdb","w")
    space = " "*9
    nums = random.sample(range(0,72),37)
    theta = 54.75
    co = 1.16
    oh = 0.96
    space = " "*6
    name = "CM  "
    
    for line in file:    
        if line.startswith("ATOM"):  
            x,y,z = float(line[30:37]), float(line[38:46]),float(line[46:54])
            nn = int(line[9:11])
            if nn not in nums:
                continue
            if x < 20 and y > 20:
                oxy = [(x+(co*math.cos(theta))),(y-(co*math.sin(theta))),z]
                oxyx = str(round(decimal.Decimal(str(oxy[0]) + '0' * 3),3))
                oxyy = str(round(decimal.Decimal(str(oxy[1]) + '0' * 3),3))
                oxyz = str(round(decimal.Decimal(str(oxy[2]) + '0' * 3),3))
                oxyl = [oxyx,oxyy,oxyz]
                hyd = [(oxy[0]+(oh*math.cos(theta))),(oxy[1]+(oh*math.sin(theta))),z]
                hydx = str(round(decimal.Decimal(str(hyd[0]) + '0' * 3),3))
                hydy = str(round(decimal.Decimal(str(hyd[1]) + '0' * 3),3))
                hydz = str(round(decimal.Decimal(str(hyd[2]) + '0' * 3),3))
                hydl = [hydx,hydy,hydz]
            elif x > 20 and y > 20:
                oxy = [(x-(co*math.cos(theta))),(y-(co*math.sin(theta))),z]
                oxyx = str(round(decimal.Decimal(str(oxy[0]) + '0' * 3),3))
                oxyy = str(round(decimal.Decimal(str(oxy[1]) + '0' * 3),3))
                oxyz = str(round(decimal.Decimal(str(oxy[2]) + '0' * 3),3))
                oxyl = [oxyx,oxyy,oxyz]
                hyd = [(oxy[0]-(oh*math.cos(theta))),(oxy[1]+(oh*math.sin(theta))),z]
                hydx = str(round(decimal.Decimal(str(hyd[0]) + '0' * 3),3))
                hydy = str(round(decimal.Decimal(str(hyd[1]) + '0' * 3),3))
                hydz = str(round(decimal.Decimal(str(hyd[2]) + '0' * 3),3))
                hydl = [hydx,hydy,hydz]
            f.write(rec.ljust(6)+str(n).rjust(5) + " " +  name.ljust(3) + atom1 + "     " + str(n).rjust(3)+space+str(oxyl[0]).ljust(8)+str(oxyl[1]).ljust(6)+str(oxyl[2]).rjust(8)+"\n")
            n += 1
            f.write(rec.ljust(6)+str(n).rjust(5) + " " +  name.ljust(3) + atom2 + "     " + str(n).rjust(3)+space+str(hydl[0]).ljust(8)+str(hydl[1]).ljust(6)+str(hydl[2]).rjust(8)+"\n")
            n += 1

