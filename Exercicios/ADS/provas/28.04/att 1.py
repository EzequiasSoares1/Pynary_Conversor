a = float(input('Qual a altura:'))
s = str(input('Qual o sexo [M/F]:')).upper()[0]

if s == 'H':
    print('O peso ideal para voçê é {:.2f}Kg'.format((72.7 * a)-58))

elif s == 'F':
     print('O peso ideal para voçê é {:.2f}Kg'.format((62.1 * a)-44.7))
