from time import sleep
d = input('Digite a senha:')
while d != '1234':
    print('processando...')
    sleep(2)
    print('Senha incorreta!!!')

    d = int(input('Digite a senha novamente:'))

print('Processando...')
sleep(2)
print('Senha correta voçê entrou:')