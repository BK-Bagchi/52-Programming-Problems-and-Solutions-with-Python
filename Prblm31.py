starting= int(input("Enter starting number: "))
ending= int(input("Enter ending number: "))
p_number=0
for number in range(starting, ending+1):
    plus=0
    for i in range(1, number):
        if number % i==0:
            plus= plus+i
        else:
            pass

    if number == plus:
        p_number+=1
        print(number, "is a perfect number")
    else:
        pass

print(f"Total {p_number} perfect numbers between {starting} and {ending}")