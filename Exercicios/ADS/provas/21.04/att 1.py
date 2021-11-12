n = int(input('Qual a quantidade de produtos:'))
list1 = []
total = []
soma = 0
for x in range(n):
    list2 = []
    for j in range(3):
        if j == 0:
             a = str(input('nome do produto:'))
             list2.append(a)
        elif j == 1:
            b = float(input('Qual o valor:'))
            list2.append(b)
        else:
            c = int(input('Qual a quantidade:'))
            list2.append(c)
          
    list1.append(list2)
    total.append(list2[2]*list2[1])

for x in range(len(total)):
    soma += total[x]
    

print('total =', soma)

        
                
                
        
