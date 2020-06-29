num1= int(input("Enter 1st number: "))
num2= int(input("Enter 2nd number: "))

min= num1
if num2<num1:
    min= num2

mul=1
for x in range(min):
    for i in range(2,min):
        if num1 % i==0 and num2 % i==0:      
            num1= int(num1/i)
            num2= int(num2/i)
            mul= mul*i
            break

mul= mul*num1*num2
    
print("LCM:", mul)