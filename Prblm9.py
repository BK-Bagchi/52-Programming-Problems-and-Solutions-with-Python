import math
num= input("Insert your number: ")
root= math.sqrt(int(num))
if math.ceil(root)== math.floor(root):
    print("Yes")
else:
    print("No")
