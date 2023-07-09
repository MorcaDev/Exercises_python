# WAY 1
#------
# basement    = int(input('Basement for stair of numbers : '))
# steps       = [1]

# for i in range(1,basement+1):
#     print(f'{steps[:]}')
#     steps.append(i+1)

# WAY 2
#------
# basement    = int(input('Basement for stair of numbers : '))
# steps       = [i for i in range(1,basement+1)]

# for i in steps:
#     print(f'{steps[0:i]}')

# WAY 3
#------
basement    = int(input('Longitud de la base : '))

for i in range(1,basement+1):

    for j in range(1,i+1):
        print(j, end=" ") 

    print(" ") 



# 1
# 12
# 123
# 1234
# .....
