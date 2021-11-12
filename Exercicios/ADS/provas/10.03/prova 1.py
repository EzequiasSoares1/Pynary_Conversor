p = str(input('Qual a categoria (A – Alimento, B - Produto de Limpeza, C – Outros):')).upper()[0]
q = int(input('Qual a quantidade:'))
Ca= 0
Cb= 0
Cc= 0
if p == 'A':
    Ca += q
elif p == 'B':
    Cb += q
elif p == 'C':
    Cc += q

while p != 'Z':
    p = str(input('Qual a categoria (A – Alimento, B - Produto de Limpeza, C – Outros):')).upper()[0]
    q = int(input('Qual a quantidade:'))
    if p == 'A':
        Ca += q
    elif p == 'B':
        Cb += q
    elif p == 'C':
        Cc += q
    elif p != 'A' or 'B' or 'C':
        print('categoria invalida')
        continue

vt = Ca + Cb + Cc
c = (Ca*100)/vt
r = (Cb*100)/vt
k = (Cc*100)/vt

print('O total de itens arrecadados foi de {}'.format(vt))
print(Ca, Cb, Cc)

if c < 50:
    print('è necessario arrecadar mais doações para a categoria de alimentos!!!')

    while c < 50 or c == 50:
        p = str(input('Qual a categoria (A – Alimento, B - Produto de Limpeza, C – Outros):')).upper()[0]
        q = int(input('Qual a quantidade:'))
        if p == 'A':
             Ca += q
        elif p == 'B':
             Cb += q
        elif p == 'C':
             Cc += q
        elif p != 'A' or 'B' or 'C':
            print('categoria invalida')
            continue

