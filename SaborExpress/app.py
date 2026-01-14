import os

restaurantes = [{'nome': 'Restaurante A', 'categoria': 'Italiana', 'ativo': True}, 
                {'nome': 'Restaurante B', 'categoria': 'Chinesa', 'ativo': False},
                {'nome': 'Restaurante C', 'categoria': 'Mexicana', 'ativo': True}]

def exibir_titulo():
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
    input("\n\nDigite uma tecla para voltar ao menu principal. ")
    main()

def exibir_subtitulo(subtitulo):
    os.system('cls')
    print(f"{subtitulo}\n")

def exibir_menu():
    print("1. Cadastrar Restaurante")
    print("2. Listar Restaurante")
    print("3. Ativar Restaurante")
    print("4. Sair\n")

def finalizar_app():

    exibir_subtitulo("Encerrando o SaborExpress...\n")

def opcao_invalida():
    print("\nOpção inválida. Tente novamente.\n\n")
    voltar_menu()

def cadastrar_novo_restaurante():
    exibir_subtitulo("Cadastro de Novo Restaurante\n")
    nome_do_restaurante = input("Digite o nome do restaurante: ")
    restaurantes.append(nome_do_restaurante)
    print(f"Restaurante {nome_do_restaurante} cadastrado com sucesso!")
    input("\nDigite uma tecla para voltar ao menu principal.")
    main()
    print(f"\nRestaurante '{nome_do_restaurante}' cadastrado com sucesso!\n")
    voltar_menu()

def Mostrar_restaurantes():
    exibir_subtitulo("Lista de Restaurantes Cadastrados\n")
    if not restaurantes:
        print("Nenhum restaurante cadastrado.")
    else:
        for idx, restaurante in enumerate(restaurantes, start=1):
            nome_restaurante = restaurante['nome']
            categoria_restaurante = restaurante['categoria']
            ativo_restaurante = "Ativo" if restaurante['ativo'] else "Inativo"
            print(f"{idx}. {nome_restaurante} | Categoria: {categoria_restaurante} | Ativo: {ativo_restaurante}")
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
                print("\nVocê escolheu ativar um restaurante.")
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