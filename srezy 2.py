print('hello world')
a = input('write your ... something!: ')
if len(a) % 2 != 0:
    print('prop_gamno')
else:
    first = a[0]
    last = a[-1]
    middle = a[1 : -1]
    print(last + middle + first)

