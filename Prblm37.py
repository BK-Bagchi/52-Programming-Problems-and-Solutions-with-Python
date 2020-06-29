inp= input("Enter a number: ")
length= len(inp)
number= int(inp)

print("Reverse number:", end=" ")
for i in range(length):
    remainder= int(number % 10)
    number= number/10
    print(remainder, end="")