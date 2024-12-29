weight=int(input("enter the weight in kg:"))
height=int(input("enter the height in cm:"))
age=int(input("enter the age:"))
gender=input("enter your gender:").lower()

if gender=="male":

    bmr=10*weight+6.25*height-5*age+5

    print(f"BMR={bmr}")

elif gender=="female":

    bmr=10*weight+6.25*height-5*-161

    print(f"BMR={bmr}")    

else:
    print("entered a wrong gender")

    

activity_level=int(input(""" select the activity level

1 for sedementery
2 for lightly active
3 for moderate active
4 for very active 
5 for extra active
"""))    

if activity_level==1:
    calories=bmr*1.2
    print(calories)

elif activity_level==2:
    calories=bmr*1.375
    print(calories)

elif activity_level==3:
    calories=bmr*1.55
    print(calories)

elif activity_level==4:
    calories=bmr*1.725
    print(calories)

elif activity_level==5:
    calories=bmr*1.9
    print(calories)

target_weight=int(input("enter the weight to reduce in kg:"))

duration=int(input("enter the duration in weeks:"))

calorie_deficit=target_weight*7700

days=duration*7

daily_calorie_deficit=calorie_deficit/days

print(f"daily calorie deficit:{daily_calorie_deficit}")