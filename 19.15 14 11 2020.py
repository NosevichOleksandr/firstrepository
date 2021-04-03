a = []
b = ''
import random
while len(a) < 101:
    a.append(random.randint(1, 70))
for i in a:
    if a.count(i) > 1:
        a.remove(i)
    for j in str(i):
        if str(j) != '2':
            b += str(j)
    if len(b) > 1:
        a.append(int(b))
    b = ''
print(a)
