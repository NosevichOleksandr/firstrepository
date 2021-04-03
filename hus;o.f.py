def countpolindroms(a):
    a += ' '
    word_or_number = ''
    answ = ''
    for i in a:
        if i != ' ':
            word_or_number += i
        elif i == ' ':
            if word_or_number == word_or_number[::-1] and len(word_or_number) > 1:
                answ += word_or_number + ' '
                word_or_number = ''
            else:
                word_or_number = ''
    return(answ)


print(countpolindroms('ablolbabc '))






        
    

    
            
    

            
    

            
            
    
