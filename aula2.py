idade = int(input ('Qual sua idade?'))
'''
if idade >= 60:
    print ('Você é um idoso, parabens!')
elif idade >= 18:
    print ('Parabens! Você pode beber e dirigir!')
else: 
    print ('Você ainda não tem idade suficiente para beber e dirigir!')
'''
'''

if idade <= 17:
    print ('Você ainda não tem idade suficiente para beber e dirigir!')
else: 
    print ('Parabens! Você pode beber e dirigir!')
    if idade >= 60:
        print ('Você é um idoso, parabens pela marca alcançada!')
'''
if idade < 12:
    print ('filmes disponivel : infantil')
elif idade > 12 and idade < 16:
    print ('filmes disponivel : infantil e juvenil')
else:
    print ('filme disponivel: infantil, juvenil e adulto')
    
ingressos_disponiveis_infantil = 20
ingressos_disponiveis_juvenil = 20
ingressos_disponiveis_adulto = 20

ingresso_comprado = input('qual ingresso você deseja comprar? ')
quantidade_de_ingressos_comprados = int (input('quantos ingressos você deseja comprar? '))

if ingresso_comprado == 'infantil':
    if ingressos_disponiveis_infantil > 0:
        print ('ingresso infantil comprado com sucesso!')
        ingressos_disponiveis_infantil -= quantidade_de_ingressos_comprados
    else:
        print ('ingressos infantis esgotados!')
        
elif ingresso_comprado == 'juvenil':
    if ingressos_disponiveis_juvenil > 0:
        print ('ingresso juvenil comprado com sucesso!')
        ingressos_disponiveis_juvenil -= quantidade_de_ingressos_comprados
    else:
        print ('ingressos juvenis esgotados!')
        
elif ingresso_comprado == 'adulto':
    if ingressos_disponiveis_adulto>0:
        print ('ingresso adulto comprado com sucesso!')
        ingressos_disponiveis_adulto -= quantidade_de_ingressos_comprados
    else:
        print ('ingressos adultos esgotados!')

print (f'ainda restam {ingressos_disponiveis_infantil} ingressos para o filme infantil')
print (f'ainda restam {ingressos_disponiveis_juvenil} ingressos para o filme juvenil')
print (f'ainda restam {ingressos_disponiveis_adulto} ingressos para o filme adulto')