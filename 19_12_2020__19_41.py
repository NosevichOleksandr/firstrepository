file = open('hype.txt', 'r')
huh = file.read()
a = 0
b = ''
for i in huh:
    if huh[a].isdigit() != True:
        b += ' '
    else:
        b += str(a)
    a += 1
print(b)
        
        
        
