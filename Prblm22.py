starting= int(input("Enter starting number: "))
ending= int(input("Enter ending number: "))
prime=0
for x in range(starting,ending+1):
    counter=0
    for i in range(2,x):
        if x % i==0:
            counter=1
            break
        else:
            counter=0
            
    if counter==0:
        prime+=1
#        print(x,"is a prime number")
    else:
        pass

print(f"Total {prime} prime numbers between {starting} and {ending}")