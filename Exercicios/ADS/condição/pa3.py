while True:
    d = float(input('Valor do emprestimo:'))
    f = int(input('Quantidade de parcelas:'))
    s = float(input('Qual o seu salario:'))

    par = d/f
    val = (30*s)/100

    if par < val:
        print('Emprestimo Aprovado')

    else:
        print('Emprestimo Negado')
