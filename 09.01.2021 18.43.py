def qw():
    file = open('0.txt' , 'r')
    smth = ''
    word = ''
    answ = 0
    for i in file:
        if i != '!' or i != ':' or i != ';' or i != "'" or i != '"' or i != '.' or i != ',':
            smth += i

    smth += ' '

    for i in smth:
        if i != ' ':
            word += i
        else:
            if len(word) % 2 == 0:
                answ += 1
            word = ''
    print(smth)
    print(answ)
    file.close()

