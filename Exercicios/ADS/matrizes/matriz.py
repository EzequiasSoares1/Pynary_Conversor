while True:
    m = int(input())
    if 0 <= m <= 15:
        lista = []

        for x in range(m):
            lista1 = []
            lista2 = 0
            for i in range(m):
               lista3= []

               if len(lista1) == 0:
                   lista1.append(+1)
                   lista2 += 1
               elif len(lista1) > 0:
                   lista3 = (lista2)*2
                   lista1.append(lista3)
                   lista2 = lista3
        lista.append(lista1)
        for c in range(len(lista)):
            list4 = []
            for i in range(len(lista)):
                d = lista[i]*2
                list4.append(d)

        lista.append(list4)

        print(lista)

    if m > 15:
        break


