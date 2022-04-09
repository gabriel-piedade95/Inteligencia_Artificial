import random as r

def abre_arquivo(file_path):

    dados = []
    with open('iris.data', 'r', encoding='utf-8') as f:

        for linha in f:

            linha = linha.split(',')
        
            vetor = [float(x) for x in linha[:4]]
            vetor.append(linha[4].strip('\n'))
            dados.append(vetor)

    return dados

