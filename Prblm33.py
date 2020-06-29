starting= int(input("Enter the starting: "))
ending= int(input("Enter the ening: "))
divisor= int(input("Enter the divisor: "))
if divisor>ending:
    print("Invalid!!")
for i in range(starting, ending+1):
    if i % divisor==0:
        print(i)