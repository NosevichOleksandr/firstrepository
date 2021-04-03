a = input('write string')
b = input('write checking letter')
c = 0
d = 0
while c < len(a):
    if a[c] == b:
        d += 1
    c += 1
print (d)
