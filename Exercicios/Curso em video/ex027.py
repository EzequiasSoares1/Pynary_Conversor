s = str(input('Digite seu nome:')).strip()
f = s.split()
print('Seu primeiro nome é {}'.format(f[0]))
print('Seu ultimo nome {}'.format(f[len(f)-1]))
