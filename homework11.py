a = [[13, 3, 'scvasd'], 33, [15,6,18,'52334']]
b = 0
for i in a:
    if isinstance(i, list):
        for j in i:
            if isinstance(j, int) and j % 2 != 0 and len(str(j)) == 2:
                b += j
print(b)
                
