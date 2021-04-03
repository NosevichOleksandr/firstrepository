string = '12.2adfa.4aisudbvo0.4'
answ = 0
for i in string:
    if i.isdigit():
        answ += float(i)
print(float(answ))
