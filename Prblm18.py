inp= input("Enter your string: ")
vowel= ["a","e","i","o","u"]
const= ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]
counter=0
length= len(inp)

for i in range(length):
    for j in range(5):
        if inp[i] == vowel[j]:
            print(inp[i], end=" ")

print()    

for i in range(length):
    for j in range(21):
        if inp[i] == const[j]:
            print(inp[i], end=" ")
            