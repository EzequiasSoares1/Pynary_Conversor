while True:
    d = int(input('Qual a quantidade de cadernos:'))

    if d % 8 == 0:

        f = d / 8
        print('São necessarias {:.0f} caixas, restaram 0 cadernos.'.format(f))

    elif d % 8 != 0:
        f = d // 8
        g = d - (f * 8)
        print('São necessarias {:.0f} caixas, restaram {} cadernos.'.format(f, g))






