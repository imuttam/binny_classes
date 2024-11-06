numbers = [1,11,43,67,51]

total = 0

# total = total + 1
# total = total+11
# total = total+43
# total = total+67
# total = total+51

# for i in numbers:
#     total = total + i
#     print("i=",i, "total=",total)

# print("Total is=",total)

count = 0
while count < 5:
    total = total + numbers[count]
    count = count + 1

print(total)
