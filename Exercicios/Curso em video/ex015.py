k = float(input('Quantos KM você dirigiu:'))
t = float(input('Quantos dias vc ficou com o carro:'))
c1 = k * 0.15
c2 = t * 60
p = c1 + c2

print('você dirigiu {:.0f}KM e ficou {:.0f} dias com o carro, o total a ser pago é de {:.2f}R$'.format(k, t, p))