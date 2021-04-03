import random
a = random.randint(1, 6)
print(a)
b = []
c = 0
while c <= a:
    b.append(c)
    b[c] = [c + 1 , []]
    c += 1
print(b)
        
    
    
