yr=int(input("Which year do you want to check ? \n"))


if (yr%4)==0:
    if (yr%100)!=0 or (yr%400)==0:
        print("This year "+ str(yr) + " is leap year")
    else:
        print("This year "+ str(yr) + " is not leap year")
else:
    print(f"This year {yr}, not leap year")



# Rakib's Comment for testing git clone and push
