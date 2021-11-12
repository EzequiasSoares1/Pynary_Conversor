n = int(input('digite o numero:'))
v = 0
while  n != 0:
    n = int(input('Digite mais um numero:'))
    if n > v:
     v = n
print('o maior numero é',v)