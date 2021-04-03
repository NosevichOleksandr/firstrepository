print('hello world!')
a = input('write your number : ')
if len(a) <= 3 :
    print('wrong number')
else:
    first = a[0]
    second = a[1]
    prelast = a[-2]
    last = a[-1]
    middle = a[2 : -2]
    print(second + first + middle + last + prelast)
