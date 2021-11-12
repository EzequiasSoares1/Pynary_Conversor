from datetime import date
a = int(input('Digite um ano qualquer:'))
d = a % 4 and a % 100 != 0 or a % 400
if a == 0:
    a = date.today().year
if d == 0:
    print('Ano de {} é bissexto'.format(a))
else:
    print('Esse ano de {} não é bissexto'.format(a))