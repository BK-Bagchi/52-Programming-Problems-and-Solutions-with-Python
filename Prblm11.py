import math
inp= input("Enter your number: ")
number= int(inp)
fact=1
for i in range(1,number+1):
    fact = fact* i

print("Manual:Factorial result: ", fact) 
print("Automatic:Factorial result: ", math.factorial(number))