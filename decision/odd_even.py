# To check weather a number is odd or even
# x = 111
# to take input from user

while True:
    x = input("Enter a number: ")# input is always a text/string
    x = int(x)

    if x == 'q':
        break

    elif x%2 == 0:
        print("Even")
    else:
        print("Odd")
                    