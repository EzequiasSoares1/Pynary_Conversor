from time import sleep
r1 = float(input('Primeiro segmento:'))
r2 = float(input('Segundo segmento:'))
r3 = float(input('Terceiro segmento:'))
print('PROCESSANDO')
sleep(3)
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print('Forma um triangulo')
else:
    print('nao forma um triangulo')