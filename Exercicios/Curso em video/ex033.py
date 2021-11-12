n1 = int(input('digite um numero:'))
n2 = int(input('digite outro numero:'))
n3 = int(input('digite mais um numero:'))

if n1 > n2 and n1 >n3:
    print('{} é o maior'.format(n1))
    if n2 < n3:
        print('{} é o menor'.format(n2))
    else:
        print('{} é o menor'.format(n3))

if n2 > n1 and n2 > n3:
    print('{} é o maior'.format(n2))
    if n1 < n3:
        print('{} é o menor'.format(n1))
    else:
        print('{} é o menor'.format(n3))

if n3 > n1 and n3 > n2:
    print('{} é o maior'.format(n3))
    if n2 < n1:
        print('{} é o menor'.format(n2))
    else:
        print('{} é o menor'.format(n1))