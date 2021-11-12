p = float(input('Preço do Produto:'))
q = int(input('Qual a quantidade:'))
d = str(input('Deseja adicionar algo S ou N:')).upper()
t = 0
m = q * p
t += m
k = (t * 12)/100
l = t + k

while d == 'S':
    p = float(input('Preço do Produto:'))
    q = int(input('Qual a quantidade:'))
    t = 0 + t
    m = q * p
    t += m
    k = (t * 12) / 100
    l = t + k
    d = str(input('Deseja adicionar algo S ou N:')).upper()


while d == 'N':
    print('O total da compra foi {:.2f}R$'.format(l))
    print('A comissão do vendedor foi {:.2f}R$'.format(k))
    print('valor sem acrescimo do vendendor {:.2f}R$'.format(t))
    break