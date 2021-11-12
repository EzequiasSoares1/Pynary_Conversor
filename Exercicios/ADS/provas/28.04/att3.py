q = int(input('qual a quantidade de peças:'))
v = float(input('Valor da peça:'))
f = q*v

if f >= 100 and f < 200:
    c = (f*10)/100
    d = f - c
    print('O valor total da compra com desconto: {}R$'.format(d))

elif f >= 200 and f < 600:
    c = (f*25)/100
    d = f - c
    print('O valor total da compra com desconto: {}R$'.format(d))

elif f >= 600:
    c = (f*50)/100
    d = f - c
    print('O valor total da compra com desconto: {}R$'.format(d))

elif f < 100:
    print('O valor total da compra : {}R$'.format(f))
