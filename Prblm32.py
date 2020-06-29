divisor= int(input("Enter the divisor: "))
rangee= int(input("Enter the range: "))
if divisor>rangee:
    print("Invalid!!")
for i in range(divisor, rangee+1):
    if i % divisor==0:
        print(i)