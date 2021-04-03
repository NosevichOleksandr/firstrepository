def calculate_symbols(a , b):
    d = 0
    c = 0
    while True:
        if d - 1 == len(a):
            break
        for i in b:
            if a[d] == i:
                c += 1
        d += 1
    return(c)
print(calculate_symbols('jnfiosnfeeifbeon' , ['a' , 'b' , 'c']))
            
    
