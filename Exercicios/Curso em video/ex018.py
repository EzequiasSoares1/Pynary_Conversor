import math
a = float(input('qual é o angulo:'))
r = math.radians(a)
d = math.sin(r)
e = math.cos(r)
f = math.tan(r)
print('o seno de {:.1f} é {:.2f} e o cosseno é {:.2f} e a tangente é {:.2f}'.format(a, d, e ,f))