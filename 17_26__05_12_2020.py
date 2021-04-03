a = 'abeafd'
b = ''
c = []
if a[::-1] != a:
    a += 'a'
for i in a:
    if i == 'a':
        c.append(b)
        b = ''
    else:
        b += i
print(c)
        
    
