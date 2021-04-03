import random
g = open('homework15.txt', 'w')
a = ['хорошего,', 'доброго,', 'плохого,']
b = ['счастливого ','удачивого ', 'депресивного']
c = 'Нового года'
d = random.randint(0,2)
e = random.randint(0,2)
f = a[d] + b[e] + c
g.write(f)
g.close()
print(f)
