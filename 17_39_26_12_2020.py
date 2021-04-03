string = '12.3asdvf64.5asdf'
counter = 0
answ = 0
smth = ''
while counter < len(string):
    if string[counter].isdigit():
        smth += string[counter]
    elif string[counter] == '.':
        smth += string[counter]
    else:
        if smth != '' and smth != '.':
            answ += float(smth)
            smth = ''
    counter += 1
print(answ)

    
    
        
