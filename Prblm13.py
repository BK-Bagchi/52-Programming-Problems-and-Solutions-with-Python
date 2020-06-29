import math
inp= input("Enter your string: ")
length= len(inp)
space=0
for i in range(length):
    if inp[i]==" ":
       space+=1
    else:
        pass

print("space:",space)
word= space+1
print("Tomi Mia's probability is: 1/",math.factorial(word))