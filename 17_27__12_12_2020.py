import random
a = int(input('hachy__strok'))
b = 0
file = open('qwerty.txt', 'w')
while b < a:
    file.write(str(random.randint(10, 12752)) + '\n')
    b += 1
file.close()
    

        
