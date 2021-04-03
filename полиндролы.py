a = int(input('write your number'))
fst = a%10
scd = a // 100 % 10
trd = a % 100 // 10
last = a//1000
if fst == last and trd == scd:
    print('da')
else:
    print ('net')
