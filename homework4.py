a = 1
b = 0
while a <= 1000:
    b += int(str(a)[-1])
    a += 1
print(b)
