file = open("access.log", 'r') 

ip_list = []

unique_ip = set()
count =0 
for line in file:
    line = line.strip().split()
    if line:
        ip_list.append(line[0])
        unique_ip.add(line[0])

print(len((ip_list)))
print(len((unique_ip)))


count = 0
while count < 20:
    for ip in unique_ip:
        print(ip, end=',')
        count += 1
        if count > 20:
            break