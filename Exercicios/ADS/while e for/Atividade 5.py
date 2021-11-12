ct= 0
c = 0
desc = 0
total = 0
quant = 0
quant2 = 0

for c in range(1,10):
    d = float(input('Qual valor da peça:'))
    e = str(input('É da coleção atual S ou N:')).upper()[0]

    if e == 'N':
        quant += 1
        t = (20*d)/100
        q = d - t
        total += d
        desc += t
        print('Seu desconto é de {:.2f}R$ e o valor total a ser pago é {:.2f}R$'.format(t, q))
        w = str(input('Deseja continuar comprando S ou N:')).upper()[0]
        if w == 'S':
            continue

        elif w == 'N':
            print('=*='*40)
            print('A quantidade de roupas compradas da coleção atual foram : {} '.format(quant2))
            print('A quantidade de roupas compradas da coleção passada foram: {} '.format(quant))
            print('Voçê tem 20% de desconto')
            print('Total sem desconto: {:.2f}R$'.format(total))
            print('Desconto obtido: {:.2f}R$'.format(desc))
            print('Total a ser pago: {:.2f}R$'.format(total-desc))
            print('=*=' * 40)
            break

    elif e == 'S':
        total += d
        quant2 += 1
        ct += d
        print('O valor total é de {:.2f}R$'.format(d))
        w = str(input('Deseja continuar comprando S ou N:')).upper()[0]

        if w == 'S':
            continue

        elif w == 'N':
            print('=*=' * 40)
            print('A quantidade de roupas compradas da coleção atual foram : {} roupas'.format(quant2))
            print('A quantidade de roupas compradas da coleção passada foram: {} roupas'.format(quant))
            print('Voçê tem 20% de desconto')
            print('Total sem desconto: {:.2f}R$'.format(total))
            print('Desconto obtido: {:.2f}R$'.format(desc))
            print('Total a ser pago: {:.2f}R$'.format(total-desc))
            print('=*=' * 40)
            break