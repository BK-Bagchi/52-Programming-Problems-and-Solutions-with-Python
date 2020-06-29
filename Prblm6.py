inp= input("Enter a number: ")
length= len(inp)
number= int(inp)
if number > 10:
    fst=int(number/(int(pow(10, length)/10)))
    last= number%10
    print("Result is: ", fst+last)
else:
    print("Result is: ", number)