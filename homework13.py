file1 = open('first.txt', 'r')
file2 = open('second.txt','r')
not_at_all = 0
smth_wrong = 0
answ = 0
completed_answ = 0
while True:
    smth = file1.read()
    anth = file2.read()

    while True:
        nothing = 0
        if smth[nothing].isdigit():
            not_at_all += smth[nothing]
            continue
        else:
            nothing += 1
            break

    while True:
        nothing = 0
        if anth[nothing].isdigit():
            smth_wrong += smth[nothing]
            continue
        else:
            nothing += 1
            break

    if not_at_all > 0 and smth_wrong > 0:
        answ = not_at_all + smth_wrong
        print(not_at_all, smth_wrong, '--->', answ)
        completed_answ += answ
        answ = 0
        not_at_all = 0
        smth_wrong = 0

    if nothing >= len(smth) and nothing >= len(anth):
        answ = not_at_all + smth_wrong
        print(not_at_all, smth_wrong, '--->', answ)
        completed_answ += answ
        answ = 0
        not_at_all = 0
        smth_wrong = 0
        break
print(completed_answ)
    
    
    
