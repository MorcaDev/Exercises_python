basement    = int(input('Base del arbol (impar) : '))
j           = int(((basement+1)/2)-1)

for i in range(1,basement+1,2):

    print(" "*j, i*"*", " "*j)
    j -= 1