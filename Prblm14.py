inp= input("Enter your string: ")
letter= input("Enter your letter: ")
counter=0
length= len(inp)
for i in range(length):
    if inp[i] == letter:
        counter+=1
    else:
        pass

if counter == 0:
    print("Your letter not found")
else:
    print("Your letter found",counter,"times")