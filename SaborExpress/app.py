import os

restaurantes = [{'nome': 'Restaurante A', 'categoria': 'Italiana', 'ativo': True}, 
                {'nome': 'Restaurante B', 'categoria': 'Chinesa', 'ativo': False},
                {'nome': 'Restaurante C', 'categoria': 'Mexicana', 'ativo': True}]

def exibir_titulo():
    '''Função para exibir o título do aplicativo'''
    print ('''
──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
─██████████████─██████████████─██████████████───██████████████─████████████████──────██████████████─████████──████████─██████████████─████████████████───██████████████─██████████████─██████████████─
─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██───██░░░░░░░░░░██─██░░░░░░░░░░░░██──────██░░░░░░░░░░██─██░░░░██──██░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░░░██───██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─
─██░░██████████─██░░██████░░██─██░░██████░░██───██░░██████░░██─██░░████████░░██──────██░░██████████─████░░██──██░░████─██░░██████░░██─██░░████████░░██───██░░██████████─██░░██████████─██░░██████████─
─██░░██─────────██░░██──██░░██─██░░██──██░░██───██░░██──██░░██─██░░██────██░░██──────██░░██───────────██░░░░██░░░░██───██░░██──██░░██─██░░██────██░░██───██░░██─────────██░░██─────────██░░██─────────
─██░░██████████─██░░██████░░██─██░░██████░░████─██░░██──██░░██─██░░████████░░██──────██░░██████████───████░░░░░░████───██░░██████░░██─██░░████████░░██───██░░██████████─██░░██████████─██░░██████████─
─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░░░██─██░░██──██░░██─██░░░░░░░░░░░░██──────██░░░░░░░░░░██─────██░░░░░░██─────██░░░░░░░░░░██─██░░░░░░░░░░░░██───██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─
─██████████░░██─██░░██████░░██─██░░████████░░██─██░░██──██░░██─██░░██████░░████──────██░░██████████───████░░░░░░████───██░░██████████─██░░██████░░████───██░░██████████─██████████░░██─██████████░░██─
─────────██░░██─██░░██──██░░██─██░░██────██░░██─██░░██──██░░██─██░░██──██░░██────────██░░██───────────██░░░░██░░░░██───██░░██─────────██░░██──██░░██─────██░░██─────────────────██░░██─────────██░░██─
─██████████░░██─██░░██──██░░██─██░░████████░░██─██░░██████░░██─██░░██──██░░██████────██░░██████████─████░░██──██░░████─██░░██─────────██░░██──██░░██████─██░░██████████─██████████░░██─██████████░░██─
─██░░░░░░░░░░██─██░░██──██░░██─██░░░░░░░░░░░░██─██░░░░░░░░░░██─██░░██──██░░░░░░██────██░░░░░░░░░░██─██░░░░██──██░░░░██─██░░██─────────██░░██──██░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─
─██████████████─██████──██████─████████████████─██████████████─██████──██████████────██████████████─████████──████████─██████─────────██████──██████████─██████████████─██████████████─██████████████─
──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────\n\n''')

def voltar_menu():
    '''Função para voltar ao menu principal'''
    input("\n\nDigite uma tecla para voltar ao menu principal. ")
    main()

def exibir_subtitulo(subtitulo):
    '''Função para exibir subtítulos'''
    os.system('cls')
    linha = '*' * len(subtitulo)
    print(linha)
    print(subtitulo)
    print(linha + "\n")

def exibir_menu():
    '''Função para exibir o menu principal'''
    print("1. Cadastrar Restaurante")
    print("2. Listar Restaurante")
    print("3. Alterar Estado do Restaurante")
    print("4. Sair\n")

def finalizar_app():
    '''Função para finalizar o aplicativo'''
    exibir_subtitulo("Encerrando o SaborExpress...")

def opcao_invalida():
    '''Função para tratar opção inválida'''
    print("\nOpção inválida. Tente novamente.\n\n")
    voltar_menu()

def cadastrar_novo_restaurante():
    '''Função para cadastrar um novo restaurante
    Inputs>
        -  Nome do restaurante
        -  Categoria

    Output>
        -  Adiciona o restaurante à lista de restaurantes

    '''
    exibir_subtitulo("Cadastro de Novo Restaurante")
    nome_do_restaurante = input("Digite o nome do restaurante: ")
    categoria = input(f"Digite a categoria do restaurante {nome_do_restaurante}: ")
    dados_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_restaurante)   # só adiciona o dicionário
    print(f"Restaurante {nome_do_restaurante} cadastrado com sucesso!")
    input("\nDigite uma tecla para voltar ao menu principal.")
    main()

def Mostrar_restaurantes():
    '''Função para mostrar os restaurantes cadastrados'''
    exibir_subtitulo("Lista de Restaurantes Cadastrados")
    if not restaurantes:
        print("Nenhum restaurante cadastrado.")
    else:
        print(f"{'NOME DO RESTAURANTE'.ljust(23)} | {'CATEGORIA'.ljust(31)} | {'STATUS'}")
        print("-" * 75)
        for idx, restaurante in enumerate(restaurantes, start=1):
            nome_restaurante = restaurante['nome']
            categoria_restaurante = restaurante['categoria']
            ativo_restaurante = "Ativo" if restaurante['ativo'] else "Inativo"
            print(f"{idx}. {nome_restaurante.ljust(20)} | Categoria: {categoria_restaurante.ljust(20)} | Ativo: {ativo_restaurante}")
    voltar_menu()

def alternar_estado_restaurante():
    '''Função para alterar o estado (ativo/inativo) de um restaurante
    
    inputs>
        -  Número do restaurante na lista para alterar o estado
    
    '''
    exibir_subtitulo("Alterar Estado do Restaurante")
    if not restaurantes:
        print("Nenhum restaurante cadastrado.")
        voltar_menu()
    else:
        for idx, restaurante in enumerate(restaurantes, start=1):
            nome_restaurante = restaurante['nome']
            ativo_restaurante = "Ativo" if restaurante['ativo'] else "Inativo"
            print(f"{idx}. {nome_restaurante} | Ativo: {ativo_restaurante}")
        try:
            escolha = int(input("\nDigite o número do restaurante para alternar seu estado: "))
            if 1 <= escolha <= len(restaurantes):
                restaurantes[escolha - 1]['ativo'] = not restaurantes[escolha - 1]['ativo']
                novo_estado = "Ativo" if restaurantes[escolha - 1]['ativo'] else "Inativo"
                print(f"Estado do restaurante {restaurantes[escolha - 1]['nome']} alterado para {novo_estado}.")
            else:
                print("Número inválido. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")
    voltar_menu()
    

try:
    def escolher_opcao():
        opcao_escolhida = int(input("Escolha uma opção: "))

        match opcao_escolhida:
            case 1:
                cadastrar_novo_restaurante()
            case 2:
                Mostrar_restaurantes()
            case 3:
                alternar_estado_restaurante()
            case 4:
                finalizar_app()
            case _:
                print("\nOpção inválida. Tente novamente.")
                opcao_invalida()

except:
    opcao_invalida()


def main():
    os.system('cls')
    exibir_titulo()
    exibir_menu()
    escolher_opcao()


if __name__ == "__main__":
    main()