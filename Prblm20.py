inp= input("Enter your string: ")
counter=0
length= len(inp)
for i in range(length):
    if inp[i] == " " or inp[i] == "! " or inp[i] == ", " or inp[i] == ". " or inp[i] == "? ":
        counter+=1
    else:
        pass

print("Total",counter+1,"words")