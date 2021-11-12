def m(lista):
    soma = 0
    media = 0
    alunos = 0

    for x in range(len(lista)):
        soma = soma + lista[x]

    media = soma / len(lista)

    for f in range(len(lista)):
        if lista[f] > media :
            alunos += 1

    print('total de alunos com notas maiores = ',alunos)


m()