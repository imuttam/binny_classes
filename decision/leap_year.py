year = int(input("Enter a year: "))

# to check divisibility by 100
if year%100 ==0:#century year
    if year%400 == 0:
        print("Year is leap year!")
    else:
        print("Year is not a leap year!")

# to check divisibility by 100
if year%100 !=0:#non century year
    if year%4 == 0:
        print("Year is leap year!")
    else:
        print("Year is not a leap year!")

#django, flask 