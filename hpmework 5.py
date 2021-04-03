a = input('sdsdsdsdsd')
if a[-1] != ' ':
    a += '  '

b = 0
c = ''
while b < len(a):
    if a[b] != ' ':
        c += a[b]
    else:
        print(c)
        c = ' '
    b += 1

        
