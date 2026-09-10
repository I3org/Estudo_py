'''
numeros = [1,2,3,4,6,17,29,'gato', True, 69]

for numero in numeros:
    print(numero)
    
print(type(numeros))

for x in range(0, 10):
    print(x)
'''
filmes = [ 'Senhor dos aneis', 'O cubo', 'Devoradores de estrelas', 'exit 8']
nota = []
 
for n in filmes:
 
   avaliacao = int(input(f'Avalie o filme {n} de 1 a 5 estrelas:') )
   if avaliacao <1 or avaliacao >5:
        print ('ERRO!: Avaliação invalida')
        break
   else:
        print (f'A nota do filme {n} foi de computada')
        nota.append(avaliacao)
    
print(f'A nota do filme {filmes[n]}')
print(f'as notas dos filmes são: {nota}')

