p = float(input('Valor do produto:'))
print('-=-'*20)
print('''[1] à vista dinheiro/cheque: 10% de desconto
[2] Á vista no cartão: 5% de desconto
[3] Em até 2x no cartão: preço formal 
[4] 3x ou mais no cartão: 20% de juros''')
print('-=-'*20)
f = int(input('Qual a forma de pagamento:'))

if f == 1:
    d = (10 * p) / 100
    vt = p - d
    print('O valor do produto com desconto de 10% é {:.2f}R$'.format(vt))

elif f == 2:
    d = (5 * p) / 100
    vt = p - d
    print('O valor do produto com desconto  de 5% é {:.2f}R$'.format(vt))

elif f == 3:
    print('O valor do produto não tem alterações. o total é {:.2f}R$'.format(p))

elif f == 4:
    d = (20 * p) / 100
    vt = p + d
    print('O valor do produto teve um acrescimo de 20%. o total é {:.2f}R$'.format(vt))

else:
    print('Forma de pagamento não existente!!!')