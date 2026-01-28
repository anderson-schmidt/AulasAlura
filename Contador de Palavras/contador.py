def limpar_texto(texto):
    '''Função para limpar o texto removendo pontuações e caracteres especiais
    Input>
        -  texto: string contendo o texto a ser limpo

    Output>
        -  texto limpo, apenas com letras e espaços

    '''
    texto=texto.lower()
    caracteres_especiais = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for char in caracteres_especiais:
        texto = texto.replace(char, '')
    return texto

def contar_palavras(frase):
    '''Função para contar o número de palavras em uma frase
    Input>
        -  frase: string contendo a frase a ser analisada

    Output>
        -  número de palavras na frase

    '''
    frase = limpar_texto(frase)
    if not frase.strip():
        return {}
    palavras=frase.split()
    contagem={}
    for palavra in palavras:
        if palavra in contagem:
            contagem[palavra] += 1
        else:
            contagem[palavra] = 1
    return contagem