# Default dict 
# A biblioteca collections nos fornece alguns formas 
# de dados alternativas bastante interessantes uma delas é a 
# defaultdict, esta forma de dados é bem parecida com um dicionário
# padrão python, porém, nos acrescenta um novo par chave-valor ao dicionário 
# criado quando buscamos uma chave que nele ainda não estava, sendo a chave deste 
# novo par acrecentado, a chave buscada anteriormente e não encontrada, e o valor, um tipo de dado
# específicado, seja um int, um float um list ou dict ou outro. 

from collections import defaultdict 

lista_palavras = ["eu", "gosto", "de", "escrever", "escrever"]


def sem_default_dict():

    contagem_palavras = defaultdict(int)

    # Sem defaultdict()

    contagem_palavras = {}

    for palavra in lista_palavras:

        if not palavra in contagem_palavras:

            contagem_palavras[palavra] = 0


        contagem_palavras[palavra] += 1


    for tupla_1_chave, tupla_2_valor in contagem_palavras.items():

        print(f"""- Palavra: {tupla_1_chave}
    - Contagem: {tupla_2_valor}""")

def com_default_dict():

    contagem_palavras = defaultdict(int)

    # O default dict irá criar um par chave-valor no dicionário buscado 
    # quando a chave ainda não faz parte dele, tendo esta como chave e 
    # um tipo ou estrutura de dados vazia específicada. 


# Exemplo 1: 

def teste_1():
    defaultdict_1 = defaultdict(int)

    print(defaultdict_1["chave_1"])

    defaultdict_1["chave_2"] = 10
    defaultdict_1["chave_3"] = 100 

    for chave, valor in defaultdict_1.items():

        print(f"""Chave: {chave}
    Valor: {valor}""")


def teste_2():

    # Agora o nosso dicionário retorna uma lista vazia. 
    defaultdict_2 = defaultdict(list)

    print(defaultdict_2["nomes"])

    defaultdict_2["idades"] = [10, 20, 30, 40]

    defaultdict_2["cidade_natal"].append("Goiânia")


    print(defaultdict_2)


# Gerando dicionarios de dicionário 
def teste_3():

    defaultdict_3 = defaultdict(dict)

    # Adiciona ao dicionário uma chave chamado pessoa_1 e a este também um chave atribuída 
    # a ela uma lista de trabalhos anteriores. 
    defaultdict_3["pessoa_1"]["trabalhos anteriores"] = ["Cientista de dados", "Engenheiro de Deep Learning"]

    defaultdict_3["pessoa_1"]["Formações"] = ["Bacharel em Ciência de dados USP", "Mestre em Deep Learning MIT"]
    print(defaultdict_3)

teste_3()