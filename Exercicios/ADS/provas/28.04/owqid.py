while True:
    print('Shopping aberto das 10Hrs as 23Hrs')
    he = float(input('horario de entrada na escala de 24h:'))
    hs = float(input('Qual o horario de saida na escala de 24h:'))

    if (he >= 10 and he < 23) and (hs >= 10 and hs < 23):
        print(he, hs)
