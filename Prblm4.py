inp= input("Enter a number: ")
number= int(inp)
print(number,"can be devied with: ", end="")
for i in range(1, number+1):
    if(number % i==0):
        print(i, " " , end="")
    else:
        pass
    
