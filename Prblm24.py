array=[]
a_length= int(input("Enter the array length: "))
for i in range(a_length):
    array.insert(i, int(input(f"array[{i}]:")))

for i in range(1, a_length+1):
    if i % 2!=0:
        print(array[i-1], end=" ")
    else:
        pass