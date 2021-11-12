v = float(input('Digite a velocidade:'))
a  = v - 80
r = a * 7
if v > 80:
    print('vc foi multado')
    print('Sua multa foi de {:.2f}R$'.format(r))

else:
    print('vc não foi multado parabens')