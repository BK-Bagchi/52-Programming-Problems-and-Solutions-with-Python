import math
number= int(input("Enter your number: "))
sum=0
for i in range(number, -1, -1):
    if i==1:
        print("2 +", end=" ")
    elif i==0:
        print("1")
    else:
        print(f"2^{i} +", end=" ")
    
    sum= sum+ math.pow(2, i)


print("Result :", int(sum))