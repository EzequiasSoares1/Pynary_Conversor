from datetime import date
d = int(input('Qual o ano que vc nasceu:'))
c = date.today().year - d

if c <= 9:
    print(' Voçê é nadador Mirim')
elif c > 9 and c <= 14:
    print(' Voçê é nadador Infantil')
elif c > 14 and c <= 19:
    print(' Voçê é nadador Junior')
elif c > 19 and c <= 20:
    print(' Voçê é nadador Senior')
elif c > 20:
    print(' Voçê é nadador Master')