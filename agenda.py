# A aplicação deve iniciar mostrando uma lista de opções do que é possível fazer com o app e permitir que o usuário digite uma escolha para iniciar a aplicação.
# Nesse desafio desenvolveremos uma agenda para salvar, editar, deletar e marcar um contato como favorito.
from time import sleep
contatos = [

]

def init():
    print('')
    print('Bem vindo a agenda de contatos!\n')
    print('1- Salvar contato')
    print('2- Editar contato')
    print('3- Deletar contato')
    print('4- Marcar contato como favorito')
    print('5- Ver contatos')
    print('6- Sair\n')

def salvar(nome_Contato, numero_Contato):
    contato = {'contato': nome_Contato,
               "numero": numero_Contato,
               "favorito": False}
    contatos.append(contato)
    print(f"Contato de {nome_Contato} adicionada")
    return

def ver(contatos):
    print('\nLista de contatos:')
    for indice, contato in enumerate(contatos, start=1):
        status = 'X' if contato["favorito"] else " "
        print(f'{indice}. [{status}] {contato['contato']} {contato['numero']}')

def editar(contatos, indice_Contato, novo_Nome, novo_Numero):
    try:
        indice_Reparado = int(indice_Contato) - 1
        contatos[indice_Reparado]["contato"] = novo_Nome
        contatos[indice_Reparado]["numero"] = novo_Numero
        print(f'Nome do contato selecionado atualizado para {novo_Nome}.\n')
        sleep(1.0)
        print(f'Numero do contato {contatos[indice_Reparado]["contato"]} atualizado para {novo_Numero}.\n')
        return
    except IndexError:
        print('Esse contato não existe, adicione o contato antes para poder editá-lo.')
        sleep(1.0)

def deletar(contatos, indice):
    try:
        indice_Reparado = int(indice) - 1
        contatos.pop(indice_Reparado)
        print('Contato removido com sucesso!')
        return
    except IndexError:
        print('Esta contato não existe, adicione o contato antes para poder remove-lo.')
        sleep(1.0)

def marcar(contatos, indice):
    try:
        indice_Reparado = int(indice) - 1
        contatos[indice_Reparado]["favorito"] = True
        print(f'{contatos[indice_Reparado]["contato"]} marcado como favorito.')
        return
    except IndexError:
        print('Esse contato não existe, adicione contatos antes para poder marcar algum como favorito.')
        sleep(1.0)

while True:
    init()
    try:
        processo = int(input('Digite a opção desejada: '))
        sleep(1.0)

        if processo == 1:
            nome_Contato = input('Digite o nome do contato: ')
            sleep(1.0)
            numero_Contato = input('Digite o número do contato: ')
            sleep(1.0)
            salvar(nome_Contato, numero_Contato)

        elif processo == 2:
            ver(contatos)
            indice = int(input('Digite o número que se situa o contato que deseja editar: '))
            sleep(1.0)
            novo_Nome = input('Digite o novo nome do contato: ')
            sleep(1.0)
            novo_Numero = input('Digite o novo número do contato: ')
            sleep(1.0)
            editar(contatos, indice, novo_Nome, novo_Numero)

        elif processo == 3:
            ver(contatos)
            sleep(1.0)
            indice_Remover = int(input('Digite o número que se situa o contato que deseja remover: '))
            sleep(1.0)
            deletar(contatos, indice_Remover)

        elif processo == 4:
            ver(contatos)
            sleep(1.0)
            indice_Favoritar = int(input('Digite o número que se situa o contato que deseja favoritar: '))
            sleep(1.0)
            marcar(contatos, indice_Favoritar)

        elif processo == 5:
            ver(contatos)

        elif processo == 6:
            break

    except ValueError:
        print('Digite um número de 1 a 6, conforme as opções listadas.\n')
        sleep(1.0)