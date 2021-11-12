n1 = int(input('digite um numero:'))
n2 = int(input('digite outro numero:'))

if n1 > n2:
    print('{} é o maior e {} é o menor'.format(n1, n2))
elif n2 > n1:
    print('{} é o maior e {} é o menor'.format(n2, n1))
elif n1 == n2:
    print('Os dois numeros são iguais')