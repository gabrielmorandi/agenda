#Gabriel Morandi de Mello - 202040602014
#Gustavo Paixão Machado - 202040602016

#criação das listas e dos dicionários e variaveis
agenda = [{'nome': 'Gustavo Paixao', 'email': 'gustavop@gmail.com', 'telefone': 949999999, 'sexo': 'm', 'idade': 19}, {'nome': 'Gabriel', 'email': 'gariel@gmail.com', 'telefone': 94977777777, 'sexo': 'm', 'idade': 19}, {'nome': 'Gustavo Paixao', 'email': 'gustavoc@gmail.com', 'telefone': 9488888888, 'sexo': 'f', 'idade': 9}]
dados_cadastro = {}
busca = []
pesquisa = []
a = 0
nome = ''
email = ''
telefone = 0
sexo = ''
idade = 0
oque = ''
deleta = []
# Criacao da funcao cadastro de contato
def cadastro_contato(nome, email, telefone, sexo, idade):
    # Cadastrar um novo contato
        # Inserindo dados no dicionário
    dados_cadastro = {'nome': nome, 
                    'email': email,
                    'telefone': telefone,
                    'sexo': sexo,
                    'idade': idade
                    }
        # Inserindo dicionpario na lista
    agenda.append(dados_cadastro)
# Criacao da funcao consultar contato
def consulta_contato(nome_contato):
    # busca pelo contato na lista de contatos ja esxistentes
    pesquisa = [p for p in agenda if p['nome'] == nome_contato]
        # se nao achar nenhum nome retornar contato nao encontrado 
    if pesquisa == []:
        pesquisa = 'Nome nao encontrado!'
        # informar se foi ou nao encontrado
    else:
        print('Contato encontrado!\n', pesquisa)
# criando a funcao para alterar o contato 
def altera_contato(nome, oque):
    # pesquisa o contato que quer alterar
    pesquisa = [p for p in agenda if p['nome'] == nome]
        # se nao achar nenhum contato retornar contato nao encontrado
    if len(pesquisa) == 0:
        print('Contato nao encontrado!')
        # se encontrar um contato ele mesmo sera alterado
    elif len(pesquisa) == 1:
        print('Contato: ', pesquisa)
        pesquisa[0][oque] = input(f'Informe o(a) novo(a) {oque} do contato: ')
        print('Contato alterado com sucesso, confira abaixo como ficou o contato!\n', pesquisa)
        # se encontrar mais de um contato igual selecione qual vai ser alterado
    elif len(pesquisa) > 1:
        print(pesquisa)
        n = int(input('Informe qual desse contatos acima voce deseja alterar (ex: para o primeiro contato digite 1, para o segundo contato digite 2): '))
        n = n - 1
        alteracao = input(f'Informe o(a) novo(a) {oque} do contato: ')
        pesquisa[n][oque] = alteracao
        if oque != 'nome':
            pesquisa = [p for p in agenda if p['nome'] == nome]
            print('Contato alterado com sucesso, confira abaixo como ficou o contato!\n', pesquisa)
        else:
            pesquisa = [p for p in agenda if p['nome'] == alteracao]
            print('Contato alterado com sucesso, confira abaixo como ficou o contato!\n', pesquisa)
# criando a funcao para excluir um contato
def excluir_contato(nome):
    pesquisa = [p for p in agenda if p['nome'] == nome]
    # se nao encontrar nenhnum contato informado 
    if len(pesquisa) == 0:
        print('Nenhum contato encontrado!')
    # se encontrar um contato informado
    elif len(pesquisa) == 1:
        print(pesquisa)
        quer = input('Deseja excluir o contato (s ou n): ')
        if quer == 's':
            i = 0
            while i != len(agenda):
                if agenda[i]['nome'] == nome:
                    deleta.append(i)
                i = i + 1
            if len(deleta) == 1:
                del(agenda[deleta[0]])
                print('Contato excluído com sucesso!')
        else:
            print('Contato NAO excluido!')
    # se encontrar mais de um contato informado
    elif len(pesquisa) > 1:
        print(pesquisa)
        n = int(input('Informe qual desse contatos acima voce deseja alterar (ex: para o primeiro contato digite 1, para o segundo contato digite 2): '))
        n = n - 1
        print(pesquisa[n])
        quer = input('Deseja excluir o contato (s ou n): ')
        if quer == 's':
            i = 0
            while i != len(agenda):
                if agenda[i]['nome'] == nome:
                    deleta.append(i)
                i = i + 1
            if len(deleta) > 1:
                del(agenda[deleta[n]])
                print('Contato excluído com sucesso!')
        else:
            print('Contato NAO excluido!')
# menu
while a == 0:
    print('========================================================')
    print('1. Cadastrar um novo contato;')
    print('2. Consultar um determinado contato;')
    print('3. Alterar os dados de algum contato;')
    print('4. Excluir um determinado contato;')
    print('5. Descobrir quantas pessoas foram cadastradas;')
    print('6. Descobrir a média de idade das pessoas;')
    print('7. Imprimir uma lista com as mulheres que estão cadastradas na agenda;')
    print('8. Imprimir uma lista com os homens que estão cadastrado na agenda;')
    print('9. Imprimir uma lista de pessoas com idade acima de um determinado número (por exemplo, imprimir uma lista de pessoas maiores de 18 anos);')
    print('10. Imprimir uma lista de e-mails cadastrados;')
    print('========================================================')
    # Escolha do usuario
    escolha = int(input('Escolha uma das opções: '))
    if escolha == 1:
        print('========================================================\nCadastre o novo contato:')
        nome = str(input('Informe o nome: ')).strip()
        email = str(input('Informe o email: ')).strip()
        telefone = int(input('Informe o telefone: '))
        sexo = str(input('Informe o sexo: ')).strip()
        idade = int(input('Informe a idade: '))
        cadastro_contato(nome, email, telefone, sexo, idade)
        print(agenda)
    elif escolha == 2:
        nome_contato = input('========================================================\nInforme o nome do contato que voce deseja pesquisar: ').strip()
        consulta_contato(nome_contato)
    elif escolha == 3:
        nome_contato = input('========================================================\nInforme o nome do contato que voce deseja alterar: ').strip()
        while oque != 'nome' and oque != 'email' and oque != 'telefone' and oque != 'sexo' and oque != 'idade':
            oque = input('Informe oque deseja alterar (nome, email, telefone, sexo, idade): ')
        altera_contato(nome_contato, oque)
    elif escolha == 4:
        nome_contato = input('Informe o nome do contato que deseja excluir: ')
        excluir_contato(nome_contato)
