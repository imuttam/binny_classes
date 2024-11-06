file = open("access.log", 'r')

writer = open("feb.txt", 'w')

for line in file:
    if ("GET /administrator" in line) and ("Feb/2016" in line):
        writer.write(line)
        



