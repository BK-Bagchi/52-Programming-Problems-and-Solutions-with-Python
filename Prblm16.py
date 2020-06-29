inp= input("Enter your string: ")
counter=0
length= len(inp)
print("Your reverse string: ", end= "")
for i in range(length-1 ,-1, -1):
    print(inp[i], end="")