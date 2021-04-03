a = input('enter string')
b = ''
c = ''
if a[-1]!= ' ':
    a += ' '
d = 0
while d < len(a):
    if a[d] != ' ':
        c += a[d]
        d += 1
        continue
    if len(c) > len(b):
        b = c
    elif len(c) == len(b):
        if c > b:
            b = c
    c = ''
    d += 1
    
print(b)
    
