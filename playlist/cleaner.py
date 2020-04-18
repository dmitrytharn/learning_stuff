def cleaning(input, output):
    with open(input) as file:
        content = file.readlines()

    new_conten = []
    for i in content:
        if ("Full Album") in i:
            j = i.replace("(Full Album)", '')
            new_conten.append(j)


    for i in new_conten:
        print(i)

    with open(output, "a+") as f:
        for i in new_conten:
            f.write(i.lstrip() + "\n")



cleaning("generated.txt", "Depressive_black.txt")
