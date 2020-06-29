string= input("Enter your string: ")
search= input("Enter your search: ")
position= string.find(search) 
if position!= -1:
    print("The search is found on:",position)
else:
    print("Your search not found")