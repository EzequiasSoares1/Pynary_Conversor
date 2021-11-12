n1 = float(input('Digite sua nota:'))
n2 = float(input('Digite Sua segunda nota:'))
r = (n1 + n2)/2

if r < 5.0:
    print('Voçê foi reprovado' )

elif r >= 5.0 and r <= 6.9:
    print('Voçê esta na recuperação')

elif r >= 7.0:
    print('Parabéns voçê foi aprovado')