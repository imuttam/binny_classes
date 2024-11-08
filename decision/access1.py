file = open("access.log", 'r') 

count = 0

lst = []
for line in file:
    count = count + 1
    line = line.split()
    if line:
    #  print(line)
        lst.append(line[0])
    # if count > 1000:
    #     break
# print(lst)
print("length of list is",len(lst))

unique_ip = set(lst)
# # print(unique_ip)
print("length of set is",len(unique_ip))