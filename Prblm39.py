def myFunction(string):
    return string[::-1]

string= input("Enter your string: ")
length= len(string)
track=0
r_string= myFunction(string)

if string== r_string:
    print("Yes! It is palindrome")
else:
    print("Sorry! It is not palindrome")