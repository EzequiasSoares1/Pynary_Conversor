def notas():
    candidatos = []

    cont = -0
    q = int(input('Qual a quantidade de candidatos:'))

    for x in range(q):
        d = input('''Digite nota e o nome
Ex= 620-Aluno:
''')
        candidatos.append(d)
        cont += 1

    candidatos.sort(reverse=True)
    c = []
    if q <= 10:
        for x in range(q):
            f = candidatos.pop(0)
            c.append(f)
    elif q > 10:
        for x in range(10):
            f = candidatos.pop(0)
            c.append(f)


    return c


print(notas())
