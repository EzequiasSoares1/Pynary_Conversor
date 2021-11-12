soma = 0
p = 0
cont = 0

for c in range(27):
    cont += 1
    n = float(input('Digite um valor:'))

    if n > p:
        p = n
        soma = soma + n

    if n > p:
        cont += c
        n = float(input('Digite um valor:'))
        soma += n
        p = n

    elif n < p:
        k = str(input('Deseja continuar, S ou N:')).upper()[0]
        soma += n
        p = n

        if k == 'N':
             p = n
             print('A media é {:.1f}'.format(soma/cont))
             break



