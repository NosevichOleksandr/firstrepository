def func(lkm):
    b = 0
    for i in str(lkm):
        b += int(i)
    return True if lkm > b**len(str(lkm)) else False
print(func(123))
