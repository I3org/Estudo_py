lista_de_alunos = []

def cadastra_aluno (nome, idade, curso, nota):
    aluno = {
        'nome': nome,
        'idade': idade,
        'curso': curso,
        'nota': [nota]
    }
    lista_de_alunos.append(aluno)
    return lista_de_alunos

def adiciona_nota (nome_do_aluno,nota_adicional):
      for aluno in lista_de_alunos:
        if aluno['nome'] == nome_do_aluno:
            aluno['nota'].append(nota_adicional)
            print(f'{nome_do_aluno } recebeu a nota {nota_adicional}')
            return

def calcula_media(nome_do_aluno):
    for aluno in lista_de_alunos:
        if aluno['nome'] == nome_do_aluno:
            media = sum(aluno['nota'])/len(aluno['nota'])
            aluno['media'] = round(media, 2)
            return
        
def exibir_aluno(nome_do_aluno):
    for aluno in lista_de_alunos:
        print(f'Nome: {aluno['nome']}, Idade: {aluno['idade']}, Curso: {aluno['curso']}, Nota: {aluno['nota']}, Média: {aluno.get('media', 'N/A')}, Situação: {aluno.get('situacao', 'N/A')}')
    return    

def avaliacao(nome_do_aluno):
    for aluno in lista_de_alunos:
        if aluno['nome'] == nome_do_aluno:
            if aluno['media'] >= 6:
                print(f'{aluno['nome']} foi aprovado com média {aluno['media']}')
                aluno['situacao'] = 'Aprovado'
            else:
                print(f'{aluno['nome']} foi reprovado com média {aluno['media']}')
                aluno['situacao'] = 'Reprovado'
    return

def relatorio_do_aluno(nome_do_aluno):
    for aluno in lista_de_alunos:
        if aluno['nome'] == nome_do_aluno:
            if 'situacao' in aluno:
             print(f'Aluno: {aluno['nome']} do curso de {aluno['curso']} consta como {aluno['situacao']}, com média {aluno['media']} ')
            else:
                print(f'Aluno: {aluno['nome']} do curso de {aluno['curso']} possui pendencias no sistema, busque seu orientador.')

cadastra_aluno ('Miguel', 20, 'Administração', 7)

cadastra_aluno ('Tulio', 25, 'Medicina', 9)

adiciona_nota ('Miguel', 5.5)
adiciona_nota ('Tulio', 8.5)
adiciona_nota ('Miguel', 6.75)
adiciona_nota ('Tulio', 9.25)

calcula_media('Miguel')


exibir_aluno('Miguel')

exibir_aluno('Tulio')

avaliacao('Miguel')

relatorio_do_aluno('Miguel')

relatorio_do_aluno('Tulio')