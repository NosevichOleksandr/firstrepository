a = input('Number')
if len(a) <= 3 :
    print('число не правильно')
else:
    first = a[0 : 2][::-1]
    last = a[-2 :][:: -1]
    middle = a[2 : -2]
    print(last +middle + first)
