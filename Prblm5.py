inp= input("Enter a number: ")
number= int(inp)
for i in range(1, number+1):
    for j in range(1, number+1):
        print("* ", end="")
    print("")