n1 = int(input('Digite um numero:'))
n2 = int(input('Digite um numero:'))
n3 = int(input('Digite um numero:'))
n4 = int(input('Digite um numero:'))



if n1 < n2 and n1 < n3 and n1 < n4:
    print(n1)
    
    if n2 > n1 and n2 < n3 and n2 < n4:
        print(n2)

    if n3 > n1 and n3 > n2 and n3 < n4:
        print(n3)
        
    if n4 > n1 and n4 > n2 and n4 > n3:
        print(n4)
        

elif n2 < n1 and n2 < n3 and n2 < n4:
    print(n2)
    
    if n1 > n2 and n1 < n3 and n1 < n4:
        print(n1)

    if n3 > n1 and n3 > n2 and n3 < n4:
        print(n3)

    if n4 > n1 and n4 > n2 and n4 > n3:
        print(n4)


elif n3 < n1 and n3 < n2 and n3 < n4:
    print(n3)

    if n1 > n3 and n1 < n4 and  n1 < n2:
        print(n1)

    if n2 > n3  and n2 < n4:
        print(n2)
        
    if n4 > n1 and n4 > n2 and n4 > n3:
        print(n4)


elif n4 < n1 and n4 < n2 and n4 < n3:
    print(n4)
    
