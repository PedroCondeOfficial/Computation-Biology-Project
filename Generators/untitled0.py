with open("output.pdb", "r") as file:
    for line in file:
        if file.startswith("ATOM"):
            