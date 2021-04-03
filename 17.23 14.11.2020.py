a = [31, 342, 120, 321, 10]
b = []
d = []
c = ''
for i in a:
    b.append(str(i)[::-1])

for i in b:
    for j in i:
        if j != 0:
            c += j
        d.append(c)
        c = ''
print(d)
           

    
