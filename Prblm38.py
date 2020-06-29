number= int(input("Enter a number: "))
length= int(input("Enter length: "))

rangee=0
for i in range(length):
    rangee+=1
    for j in range(rangee):
        print(number, end=" ")
    print()

for i in range(length-1):
    rangee-=1
    for j in range(rangee):
        print(number, end=" ")
    print()