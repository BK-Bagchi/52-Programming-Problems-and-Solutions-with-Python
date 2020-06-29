import math
inp= input("Enter your number: ")
length= len(inp)
number= int(inp)
store=[]
for i in range(length):
    reminder= number % 10
    store.insert(i+1, reminder)
    number= int(number /10)

store.reverse()
sum=0
for i in range(length):
    sum= sum+math.pow(store[i], length)
    

if int(inp) == int(sum):
    print(inp,"is an armstrong number")
else:
    print(inp,"is not an armstrong number")