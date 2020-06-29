number= int(input("Enter your number: "))
plus=0
for i in range(1, number):
    if number % i==0:
        plus= plus+i
    else:
        pass

if number == plus:
    print(number, "is a perfect number")
else:
    print(number, "is not a perfect number")    