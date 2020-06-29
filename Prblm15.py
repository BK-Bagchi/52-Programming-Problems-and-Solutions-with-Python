inp= input("Enter your string: ")
letter= ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
counter=0
length= len(inp)
for i in range(26):
    for j in range(length):
        if letter[i] == inp[j]:
            counter+=1
    if counter != 0:
        print(letter[i],"found", counter, "times")
    counter=0