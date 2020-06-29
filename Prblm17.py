inp= input("Enter your string: ")
letter= ["a","e","i","o","u"]
counter=0
length= len(inp)
for i in range(5):
    for j in range(length):
        if letter[i] == inp[j]:
            counter+=1

print("Number of vowles: ", counter)