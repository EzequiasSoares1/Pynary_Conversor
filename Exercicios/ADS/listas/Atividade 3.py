lista = []
lista2 = []
for x in range(20):
    g = int(input('Digite um numero inteiro:'))
    if len(lista) <= 9:
        if (g not in lista):
            print(' Adicionado na lista 1')
            lista.append(g)
        else:
            print('Numero repetido')

    else:
        if (g not in lista2):
            print('Adicionado na lista 2')
            lista2.append(g)
            if (g not in lista):
                lista.append(g)
        else:
            print('Numero repetido')

print('O conjunto união é {}'.format(lista))






