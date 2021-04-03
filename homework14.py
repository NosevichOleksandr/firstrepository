file = open('123.txt', 'r')
answer = ''
for i in file:
    if i.isdigit():
        answer += i
    else:
        answer += ' '
print(answer)
        
        
        
    
