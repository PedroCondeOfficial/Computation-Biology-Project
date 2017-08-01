with open("output.pdb","r") as file: 
    k = open("secout.pdb", "w")
    for line in file:
        k.write(line)
    k.close()