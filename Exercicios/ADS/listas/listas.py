fila1 = []
fila2 = []
n1 = len(fila1)
n2 = len(fila2)
for x in range(0,4):
    d = str(input('Digite seu nome:'))
    h = str(input('É priotitario S ou N:')).upper()[0]

    if h == 'S':
        fila1.append(d)

    elif h == 'N':
        fila2.append(d)

for l in fila(len(fila1)):


