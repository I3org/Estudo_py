conjunto_teste = set()

conjunto_teste.add(1)
conjunto_teste.add(2)
conjunto_teste.add('gato')
conjunto_teste.add('arara')
print(conjunto_teste)
conjunto_teste.remove('arara')
conjunto_teste.add(1) 
#conjunto não permite duplicidade de elementos

print(conjunto_teste)

def identifica_elemento(conjunto, elemento):
    if elemento in conjunto:
        print(f'O elemento {elemento} está presente no conjunto.')
    else:
        print(f'O elemento {elemento} não está presente no conjunto.')
        
identifica_elemento(conjunto_teste, 'gato')
identifica_elemento(conjunto_teste, 'arara')

itens = ['ovo', 'leite', 'farinha', 'ovo', 'açúcar', 'leite']
itens_unicos = set(itens)

print(itens)
print(itens_unicos)





