def soma(val,val1,val2):
    soma1 = val + val1

    if soma1 == val2:
        print('A soma de {} + {} é igual a {}'.format(val, val1, val2))
    elif soma1 < val2:
        print('A soma de {} + {} é menor que {}'.format(val, val1, val2))
    elif soma1 > val2:
        print('A soma de {} + {} é maior que {}'.format(val, val1, val2))

soma()