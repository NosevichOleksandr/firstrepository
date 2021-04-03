a = []
b = 0
for i in range(1,1001):
    a.append(i)
    if str(0) in str(i):
        b += 1
print(b)
