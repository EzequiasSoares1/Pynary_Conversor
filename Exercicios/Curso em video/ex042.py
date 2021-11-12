n1 = int(input('Primeiro segmento:'))
n2 = int(input('Segundo segmento:'))
n3 = int(input('Terceiro segmento:'))

if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 +n2:
    print('Forma um triangulo')

    if n1 == n2 and n1 == n3:
        print('È um triângulo EQUILÁTERO')

    elif n1 == n2 or n1 == n3 or n2 == n3 or n2 == n1 or n3 == n2 or n3 == n1:
        print('È um triângulo ISÓCELES')

    else:
        print('È um triângulo ESCOLENO')

else:
    print('Não forma um Triângulo')