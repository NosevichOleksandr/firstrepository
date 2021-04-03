data = [1, 2, 3, [2, 3, '12'], [123], 22, [1, 2]]
answer = []
for i in data:
    if isinstance(i,list):
        answer.extend(i)
    else:
        answer.append(i)
print(answer)
