
print('*=*'*30)
print('''                                Bem Vindo
[1]Conversão de Bases numericas:
[2]Aritimetica Binaria:
''')
print('*=*'*30)

c = int(input('Deseja fazer qual operação [1/2]:'))

if c == 1:
    print('*=*' * 30)
    print('''
[1]Binaria para Decimal:
[2]Decimal para Binaria:
   ''')
    print('*=*' * 30)

    d = int(input('Digite a base de conversão:'))
    if d == 1:
        i = str(input('Digite o numero em Binario:'))
        num = int(i, 2)
        float(num)
        print('---' * 30)
        print('O Binario {} em Decimal é : {}'.format(i, num))
        print('---' * 30)

    elif d == 2:
        de = int(input('Digite o numero em Decimal:'))
        n = bin(de)
        print('---' * 30)
        print('O Decimal {} em Binario é : {}'.format(de, n[2:]))
        print('---' * 30)
elif c == 2:

    print('*=*' * 30)
    print('''
[1] Adição: +
[2] Subtração: - 
[3] Divisão: / 
[4] Multiplicação: *
    ''')
    print('*=*' * 30)

    d1 = int(input('Deseja fazer qual operação [1/2/3/4]:'))

    if d1 == 1:
        b1 = str(input('Digite o numero em Binario:'))
        num1= int(b1, 2)
        float(num1)
        b2 = str(input('Digite o numero em Binario:'))
        num2 = int(b2, 2)
        float(num2)
        soma = num1 + num2
        s1 = bin(soma)
        print('---' * 30)
        print('{} + {} = {}'.format(b1, b2,s1[2:]))
        print('---' * 30)
    elif d1 == 2:
        b1 = str(input('Digite o numero em Binario:'))
        num1 = int(b1, 2)
        float(num1)
        b2 = str(input('Digite o numero em Binario:'))
        num2 = int(b2, 2)
        float(num2)
        soma = num1 - num2
        s1 = bin(soma)
        print('---' * 30)
        print('{} - {} = {}'.format(b1, b2, s1[2:]))
        print('---' * 30)

    elif d1 == 3:
        b1 = str(input('Digite o numero a ser dividido em Binario:'))
        num1 = int(b1, 2)
        float(num1)
        b2 = str(input('Digite o numero divisor em Binario:'))
        num2 = int(b2, 2)
        float(num2)
        soma = int(num1 / num2)
        s1 = bin(soma)
        print('---' * 30)
        print('{} / {} = {}'.format(b1,b2,s1[2:]))
        print('---' * 30)

    elif d1 == 4:
        b1 = str(input('Digite o numero em Binario:'))
        num1 = int(b1, 2)
        float(num1)
        b2 = str(input('Digite o numero em Binario:'))
        num2 = int(b2, 2)
        float(num2)
        soma = num1 * num2
        s1 = bin(soma)
        print('---' * 30)
        print('{} * {} = {}'.format(b1, b2, s1[2:]))
        print('---' * 30)

    else:
        print('valor invalido')

