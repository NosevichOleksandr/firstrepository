import random
def randomm(a , b , c):
    file = open('qwerty.txt' , 'w')
    for i in range(0 , a):
        file.write(str(random.randint(b , c)) + ' ')
    file.close()
    return


file = open('qwerty.txt' , 'r')
filie = file.read()
file.close()
r = ''
answ = []
for i in filie:
    if i.isdigit() and len(r) == 0:
        r += i
    if i == '+' and r != '' and '+' not in r:
        r += i
    if i.isdigit() == False and i != '+':
        r = ''
    if len(r) == 3:
        answ.append(int(r[0]) + int(r[2]))
print(answ)
            
        
            
            
    
