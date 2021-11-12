cl = []
clp = []

for x in range(20):
    c = str(input('Digite o nome:'))
    p = str(input('É prioritario S ou N:')).upper()[0]

    if p == 'S':
        clp.append(c)

    elif p == 'N':
        cl.append(c)
    else:
        print('Não reconheço essa resposta')
        continue

while len(cl) or len(clp) >= 0:

    if len(cl) and len(clp) != 0:
        n1 = cl.pop(0)
        n2 = clp.pop(0)
        print(n1)
        print(n2)

    elif len(cl) > 0:
        n1 = cl.pop(0)
        print(n1)

    elif len(clp) > 0:
        n2 = clp.pop(0)
        print(n2)


