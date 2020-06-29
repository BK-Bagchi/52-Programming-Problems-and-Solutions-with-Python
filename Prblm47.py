length1= int(input("Length array 1: "))
length2= int(input("Length array 2: "))

a=[]
b=[]
c=[]
print("Enter into 1st array: ")
for i in range(length1):
   a.insert(i,int(input(f"a[{i+1}]= ")))

print("Enter into 2nd array: ")
for i in range(length2):
   b.insert(i,int(input(f"b[{i+1}]= ")))

c= a+b
c.sort()
print(c)