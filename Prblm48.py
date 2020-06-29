length= int(input("Length: "))

a=[]
store= []
call= 0; no=0

print("Enter into 1st array: ")
for i in range(length):
   a.insert(i,int(input(f"a[{i+1}]= ")))


def callYes(call):
    print('Missed number(s): ', end=" ")


for i in range(1, length+1):
    for j in range(length):
        if i!=a[j]:
            check=1
        else:
            check=0
            break
    if check==1:
        if call==0:
            callYes(call)
            call+=1; no=1
        print(i, end=" ")
    else:
        pass
    
if no==0:
    print("No missing number")