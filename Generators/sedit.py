with open("sOH.pdb","r") as file:
    g = open("sp.pdb","a")
    
    for line in file:
        g.write(line)
    g.close()

