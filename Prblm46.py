import math
a= int(input("Hand 1: "))
b= int(input("Hand 2: "))
c= int(input("Hand 3: "))
s= (a+b+c)/2
area= math.sqrt(s*(s-a)*(s-b)*(s-c))
print("Area of the triangle is:", area)