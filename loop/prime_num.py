num =  12

prime = True
for i in range(2, num):  # 2,3,4,5,6,7,8
    if num%i == 0:
        prime = False

if prime == True:
    print(num, "is a prime number")

else:
    print(num, "is not a prime number")
    