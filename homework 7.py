a = []
b = 0
while len(a) < 124:
    if '2' in str(b) and '7' in str(b) and b%2 != 0:
        a.append(b)
    if '2' in str(b):
        a.remove(a[-1])
    
    b += 1
#a.reverse
print(a)

    
