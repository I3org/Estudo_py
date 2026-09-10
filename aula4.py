numero_prim = []

def numeros_primos (n):
    if n<=1 :
        return f'{n} é um número primo'
    
    for i in range(2, n):
        if n % i == 0:
            return f'{n} não é um número primo'

    numero_prim.append(n)
    
    return f'{n} é um número primo'

numeros =range(1, 100)

for i in numeros:
    print (numeros_primos(i))
    
print (numero_prim)