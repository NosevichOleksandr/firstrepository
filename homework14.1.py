file = open('qwer.txt', 'r')
number = ''
hmmm = 0
answ = 0
for i in file:
    if i.isdigit():
        number += str(i)
    elif i.isdigit == False:
        answ += int(number)
        hmmm += str(number) + '+'
        number = ''
print(hmmm , answ)

        
    
        
    
