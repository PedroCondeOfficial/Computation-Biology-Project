with open("OH.pdb", "r") as file:
    k = open("output.pdb","a")

    for lines in file:
            k.write(lines)
    file.close()            