import math
base= int(input("Enter the base: "))
power= int(input("Enter the power: "))
sum=0
for i in range(power+1):
    sum= sum+ math.pow(base, i)

print("Result= ",int(sum))