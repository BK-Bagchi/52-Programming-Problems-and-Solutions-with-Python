inp= input("Enter a character: ")

if 48<= ord(inp[0]) <=57: #48 57   65 90   97 122
    print("Its a number")
elif 65<= ord(inp[0]) <=90:
    print("Its a uppecase letter")
elif 97<= ord(inp[0]) <=122:
    print("Its a lowercase letter")
else:
    print("Its a special character")