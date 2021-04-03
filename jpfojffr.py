def words(a):
    b = 0
    c = 0
    while True:
        if b - 3 == len(a):
            break
        if a[b] == ' ' or a[b] == '?' or a[b] == '.' or a[b] == ',' or a[b] == '!' or a[b] == ',' or a[b] == '-' or a[b] == ';' or a[b] == ':':
            c += 1
        b += 1
print(words('alhhjvgy jv vh bilb  luvhv'))
        
  
