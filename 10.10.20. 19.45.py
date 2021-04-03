a = input('enter your string')
b = 0
c = 0
while b < len(a):
    if a.isdigit():
        if a%2 == 0:
            c += 1
    b += 1
print(c)
