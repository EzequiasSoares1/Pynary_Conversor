p = float(input('Qual o seu peso:'))
a = float(input('Qual sua altura:'))
m = p / (a**2)

print('Seu IMC é de {:.2f} de massa corporia'.format(m))

if m < 18.5:
    print('Abaixo do Peso')

elif m >= 18.5 and m < 25:
    print('Peso Ideal')

elif m >= 25 and m < 30:
    print('Sobrepeso')

elif m >= 30 and m <= 40:
    print('Obesidade')

else:
    print('Obesidade Mórbida')
