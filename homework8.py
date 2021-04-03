a = []
b = 0
import random
while len(a) < 101:
    a.append(random.randint(100, 250))

for i in a:
    if a.count(i) > 1:
        a.append(random.randint(100, 250))
        a.remove(i)

for i in a:
    b += i
    
print(len(a))
print(b)
