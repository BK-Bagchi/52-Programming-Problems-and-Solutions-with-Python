array=[]
a_length= int(input("Enter the array length: "))
for i in range(a_length):
    array.insert(i, input(f"array[{i}]:"))

array.sort()
for i in array:
    print(i)