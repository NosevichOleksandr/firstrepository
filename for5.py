b = input('enter string')
c = 0
for i in b:
    if i in '.' or ',' or ';' or ':' or '-':
        c += 1
print(c)
