a = int(input('number'))
answ = 0
while True:
    if a%2 == 0:
        a = a//2
        answ += 1
    else:
        break
print(answ)

