ct= 0
c = 0
d = 0

for c in range(1,10):
    d = float(input('Qual valor da peça:'))
    e = str(input('É da coleção atual S ou N:'))upper()
    if e == 'N':
        t = (20*d)/100
        q = d - t
        c += q
        print('Seu desconto é de {} e o valor total a ser pago é {}'.format(t, q))
        w = str(input('Deseja continuar S ou N:'))upper()
        if w == 'S':
            continue
        elif w == 'N':
            break
    elif e == 'S':
        ct += d
        print('O valor total é de {}'.format(d))
        w = str(input('Deseja continuar S ou N:'))upper()
        if w == 'S':
            continue
        elif w == 'N':
            break