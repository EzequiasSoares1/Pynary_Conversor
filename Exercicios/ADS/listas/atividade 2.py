fila = []
fila2 = []
fila3 = []

for x in range(15):
    d = str(input('Digite um nome:'))
    fila.append(d)
    if len(fila) > 5:
        f = fila.pop(0)
        fila2.append(f)

    if len(fila2) > 5:
        f = fila2.pop(0)
        fila3.append(f)

    print('fila 1:', fila)
    print('fila 2:', fila2)
    print('fila 3:', fila3)

while len(fila3) > 0:
    print('-=-'*30)
    g = input('Click enter')
    print('-=-'*30)

    if g == '':
        if len(fila) > 0:
             f = fila.pop(0)
             fila2.append(f)

        if len(fila2) > 0:
            f = fila2.pop(0)
            fila3.append(f)

        f = fila3.pop(0)

        print('fila 1:', fila)

        print('fila 2:', fila2)

        print('fila 3:', fila3)
    else:
        continue

print('Filas vazia')


