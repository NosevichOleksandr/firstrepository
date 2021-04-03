file = open('second.txt', 'r')
data = file.readlines()
file.close()
file2 = open('first.txt', 'r')
data2 = file2.readlines()
file2.close()

long = data if len(data) > len(data2) else data2
short = data if len(data) < len(data2) else data2
file2 = open('first.txt', 'a')
file = open('second.txt', 'a')
for i in range(len(long) - len(short)):
    short.append('/n')






file = open('lol2.txt', 'w')
for i in range(len(long)):
    if i < len(short):
        file.write(str(int(long[i]) + int(short[i])) + '\n')
        continue
