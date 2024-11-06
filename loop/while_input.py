
count = 1
while True:
    user = input("Enter your  user name: ")

    print("hello", user)
    password = input("Enter your  password: ")
    count = count + 1
    if password == 'letmein':

        print("You are in")
        break
    elif count == 3:
        print("You are out of attempt!")
        break
    else:
        print("password is wrong!")

