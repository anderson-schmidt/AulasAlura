from contador import contar_palavras

frase = input("Digite uma frase: ").strip
if not frase:
    print("A frase está vazia.")
else:
    resultado = contar_palavras(frase)
    if resultado:
        print("Contagem de palavras:")
        for palavra, contagem in resultado.items():
            print(f"'{palavra}': {contagem}")
        else:
            print("Nenhuma palavra encontrada na frase.")
