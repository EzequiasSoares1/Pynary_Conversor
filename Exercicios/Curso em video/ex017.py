import math
co = float(input('DIGITE O COMPRIMENTO DO CATETO OPOSTPO:'))
co1 = float(input('DIGITE O COMPRIMENTO DO CATETO ADJACENTE:'))
hi = math.hypot(co, co1)
print('o resultado é:{:.2f}'.format(hi))