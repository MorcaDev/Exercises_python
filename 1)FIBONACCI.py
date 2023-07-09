length  = int(input('Numero de sumas : '))

num_a   = 0
num_b   = 1
print(num_a, end=", ")
print(num_b, end=", ")

for i in range(length):
    
    num_c = num_a + num_b
    print(num_c, end = ', ')
    
    num_a = num_b
    num_b = num_c