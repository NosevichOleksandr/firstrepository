a = input('1st string')
b = input('2nd string')
c = ''
for i in a:
    if i in b:
        c += i
print(c)
