a = open('homework16.1.txt', 'r')
b = open('homework16.2.txt', 'r')
poryadok = a.read()
wh = b.read()
a.close()
b.close()
true_wh = []
shed = ''

for i in wh:
    if i != ' ':
        shed += i
    elif i == ' ':
        true_wh.append(shed)
        shed = ''

true_poryadok = []
for i in poryadok:
    if i != ' ':
        true_poryadok.append(int(i)-1)

hw = []
a = 0
for i in true_poryadok:
    hw.append(true_wh[true_poryadok[a]])
    true_wh.remove(true_wh[true_poryadok[a]])
    a += 1
print(hw)
    
    
    
    



    
    
    
