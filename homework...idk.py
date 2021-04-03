def func(b):
    answ = ''
    if b.isdigit():
        return b
    else:
        for i in str(b):
            if i.isdigit() == False:
                answ += i
    return answ
print(func('abc3'))

