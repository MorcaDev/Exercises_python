
altura = int(input('Altura de la piramide : '))

for i in range(1,altura+1,1):
    print(i*'*')

for j in range(altura-1,0,-1):
    print(j*"*")