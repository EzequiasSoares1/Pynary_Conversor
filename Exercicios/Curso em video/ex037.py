n1 = int(input('digite um numero inteiro:'))
print(''' bases de conversão:
[1]Binaria
[2]Octal
[3]Hexadecimal:''')
c = int(input('digite a base de conversão:'))

if c == 1:
    print('{} em binario é {}'.format(n1, bin(n1)[2:]))
elif c == 2:
    print('{} em Octal é {}'.format(n1, oct(n1)[2:]))
elif c == 3:
    print('{} em Hexadecimal é {}'.format(n1, hex(n1)[2:]))
else:
    print('Opção escolhida nao existe')

