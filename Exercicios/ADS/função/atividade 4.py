def media():
    n = 0
    cont = 0

    while cont < 3:
        if cont == 0:
            n1 = int(input('Digite a primeira nota:'))
            if n1 > 0 and n1 <= 10:
                 n += n1
                 cont += 1
            else:
                print('Valor invalido')

        elif cont == 1:
            n1 = int(input('Digite a segunda nota:'))
            if n1 > 0 and n1 <= 10:
                n += n1
                cont += 1
            else:
                print('Valor invalido')

        elif cont == 2:
            n1 = int(input('Digite a terceira nota:'))
            if n1 > 0 and n1 <= 10:
                n += n1
                cont += 1
            else:
                print('Valor invalido')

    m = n/3
    if m >= 7:
        print('APROVADO')
    elif m < 7:
        print('REPROVADO')

media()