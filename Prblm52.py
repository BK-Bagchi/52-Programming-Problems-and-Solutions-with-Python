string= input("Enter your string: ")
search= input("Enter your search: ")
length= len(string)
counter=0
sett=0
for i in range(length):
    position= string.find(search, sett, length) 
    if position!= -1:
#        print("P", position)
        sett= position+1
        counter+=1
    else:
        sett+=1
    
if counter!= 0:
    print("The search is found:",counter,"times")
else:
    print("Your search not found")