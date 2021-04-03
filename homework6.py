for i in range(0,201,2):
    if str(i)[:: -1] != 2:
        if str('0') not in str(i):
            print(i)
