from collections import Counter

# Counter

# Os counters são uma forma inteligente de contar quantas vezes um item aparece 
# em um iterável, no caso uma lista, ele cria um dicionário onde com pares onde 
# a chave é o item que está sendo contado e o valor a quantidade de vezes que 
# o elemento aparece no iterável. 

lista_textos = ["programação", "em","c", "python", "programação", "em", "linguagem", "c", "c", "Python", "c"]

contador = Counter(lista_textos)

def mostrar_counter_a():
    contador_tupla = list(contador.items())

    # Ordenando por quantidade de aparições. 

    # O método sorted() não altera a lista original
    ordenacao_tuplas = sorted(contador_tupla, key= lambda tupla: tupla[1], reverse= True)

    for tupla in ordenacao_tuplas:
        print(f"""Palavra: {tupla[0]}
    Contagem: {tupla[1]}""")


def mostrar_counter_b():

    # A função moust_common() nos retorna uma tupla ordenada com 
    # os pares chaves-valor em ordem decrescente.

    aparicoes_mais_comuns = contador.most_common()

    # print(aparicoes_mais_comuns)  
    for palavra, quantidade_aparicoes in aparicoes_mais_comuns:
        
        print(f"""Palavra: {palavra}
Quantidade de aparições: {quantidade_aparicoes}""")


# mostrar_counter_b()


# Utilizando a função enumerate()

