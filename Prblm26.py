food_of_days= int(input("Enter food of days: "))
food_of_kg= int(input("Enter food of kg: "))
food_given_per_day= food_of_kg/food_of_days
food_need_per_day= food_given_per_day/2
days=0
for i in range(food_of_kg*2):
    if food_of_kg <=1:
        break
    else:
        food_of_kg -=food_need_per_day
        days+=1

print("Gupi can stay",days,"days with",food_of_kg,"kg of food")
