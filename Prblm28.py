array= []
a_len= int(input("Enter array length:"))
for i in range(a_len):
    array.insert(i, int(input(f"array[{i+1}]:")))

sorted_array= array.copy()
sorted_array.sort()

if sorted_array==array:
    print("This array is sorted")
else:
    print("This array is not sorted")
