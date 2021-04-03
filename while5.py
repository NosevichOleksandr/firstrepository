a = 1
while a < 10000:
    b = a
    a = a + 1
    if b%7 == 0 and b%5 == 0:
        b += 1
print(b)
        
