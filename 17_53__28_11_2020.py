a = []
b = 0
import random
while len(a) < 20:
    a.append(random.randint(1,7))
for i in a:
    b += 1
    if isinstance(i, list) == False:
        a[b : i] = [b, i],
print(a)


