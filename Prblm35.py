import math
xc= float(input("Enter the central X: "))
yc= float(input("Enter the central Y: "))
r= float(input("Enter the radious: "))
xl= float(input("Enter the point X: "))
yl= float(input("Enter the point Y: "))

result= math.sqrt( math.pow((xc-xl),2) + math.pow((yc-yl),2) )

if result>r:
    print("The point is outide the circle")
elif result==r:
    print("The point is on the circle")
else:
    print("The point is inside the circle")