string= input("Enter your string(with L&R):")
string2= []
length= len(string)
for i in range(length):
    string2.insert(i, string[i])
for i in range(length):
    if string2[i]=="L" and i==0:
        string2[i]= "0"
    elif string2[i]=="R" and i== length-1:
        string2[i]= "0"
    elif string2[i]=="L":
        string2[i]= string2[i-1]
    elif string2[i]=="R":
        string2[i]= string2[i+1]
    else:
        pass

string= "".join(string2)
print(string)