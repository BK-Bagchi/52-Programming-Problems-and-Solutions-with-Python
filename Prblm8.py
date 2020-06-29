numbers=[]
for i in range(6):
    numbers.insert(i, input(f"a[{i+1}]= "))

min= numbers[0]
for i in range(1,6):
    if numbers[i]<min:
        min= numbers[i]
    else:
        pass


print("Manually: Minimum number is: ",min)