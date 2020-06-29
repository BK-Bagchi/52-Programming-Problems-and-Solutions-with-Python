inp= input("Enter your letter: ")
length= len(inp)
letter= inp.lower()
print("Letter converted into number:", end=" ")
for i in range(length):
    print(ord(letter[i])-96, end="")