print('hello world')
a = input('write first number')
b = a[:: -1]
c = 0
while c < len(a):
    print(b[c])
    c += 1
    
