print('hello world')
a = input('write first number')
b = input('write second number')
c = 0
d = 0
while c < len(a):
    if a[c] in b:
        d += 1
    c += 1
print (d)
