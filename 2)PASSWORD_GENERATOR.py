import random
import string

password_len    = int(input('Longitud de la clave : '))
password        = ""
categories      = [string.ascii_letters, string.digits]

for i in range(password_len):
    category   = random.choice(categories)
    value      = random.choice(category)
    password   += value
    
print(password)