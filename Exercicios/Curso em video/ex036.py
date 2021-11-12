c = float(input('Qual valor da casa:'))
a = float(input('Quantos anos para pagamento:'))
s = float(input('Qual valor do seu salario:'))
c1 = a * 12
c2 = c/c1
c3 = (s*30)/100
if c2 <= c3:
    print('Para pagar a casa de {:.2f}R$ em {:.0f} anos a prestaçaõ sera de {:.2f}R$'.format(c, a, c2))
    print('Seu emprestimo foi aprovado')
elif c2 > c3:
    print('Para pagar a casa de {:.2f}R$ em {:.0f} anos a prestaçaõ sera de {:.2f}R$'.format(c, a, c2))
    print('seu emprestimo nao foi aprovado')