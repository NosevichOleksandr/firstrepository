a = 0
b = 0
while a < 1000:
    b = b + 1
    if b%2 == 0 and b%3 != 0:
        a += 1
        print(b)
        
