inp= input("Enter your numbers: ")
counter=0
length= len(inp)
for i in range(length):
    if inp[i] == " ":
        counter+=1
    else:
        pass

print("Total",counter+1,"numbers")