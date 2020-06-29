import math
number= int(input("Enter your number: "))
fact= math.factorial(number)
length= len(str(fact))
count=0
for i in range(length-1):
    if fact % 10==0:
        count+=1
    else:
        break
    fact /= 10
print("Number of zeros at the end of factorial result:",count)