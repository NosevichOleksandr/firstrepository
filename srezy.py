print('hello world')
a = input('write your ... something: ') 
if len(a) % 2 == 0:
    b = a[:len(a)//2]
    c = a[len(a)//2:][::-1]
    print(b + c)
else:
    print('ты неправильно ввел')
