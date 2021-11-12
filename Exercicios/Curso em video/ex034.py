s = float(input('Digite seu salario:'))

if s <= 1250:
    v = (15 * s) / 100
    a = s + v
    print('Seu salário teve um acrescimo de 15%, o total é {:.2f}R$ '.format(a))

else:
    v = (10 * s) / 100
    a = s + v
    print('Seu salário teve um acrescimo de 10%, o total é {:.2f}R$ '.format(a))


