soma = temp1 = temp2 = 0
for c in range(27):
    n = int(input('Digite um valor: '))
    soma += n
    temp1 = n
    if temp1 > temp2 and c > 0:
        temp2 = n
        g = soma / c
        d = str(input('Deseja continuar: ')).upper()
        if d == 'S' or d == 'SIM':
            continue
        elif d == 'N' or 'NÃO' or 'NAO':
            print('A media é {}'.format(g))
            break