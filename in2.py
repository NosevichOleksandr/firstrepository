print('hello world')
a = input('write first number')
b = 0
c = 0
while b < len(a):
    if a[b].isdigit():
        c += int(a[b])
    b += 1
print(c)
    
