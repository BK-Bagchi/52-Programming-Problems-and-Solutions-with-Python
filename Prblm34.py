divisor1= int(input("Enter the 1st divisor: "))
divisor2= int(input("Enter the 2nd divisor: "))
ending= int(input("Enter the ening: "))
if divisor1>ending or divisor2>ending:
    print("Invalid!!")
for i in range(1, ending+1):
    if i % divisor1==0 and i % divisor2==0:
        print(i)