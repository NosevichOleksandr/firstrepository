data = data = [1, 2, ['234', 2], [34, [12, '3452'], 12], [123]]
data2 = []
answer= []
for i in data:
    if isinstance(i,list):
        data2.extend(i)
    else:
        data2.append(i)


for i in data2:
    if isinstance(i,list):
        answer.extend(i)
    else:
        answer.append(i)
print(answer)
