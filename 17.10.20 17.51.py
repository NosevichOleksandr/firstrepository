a = input("we'll steal your data")
stroki = ''
chisla = ''
for i in a:
    if i.isdigit():
        chisla += i
    else:
        stroki += i
print(chisla)
print(stroki)
