# Importações 

from faker import Faker
import random 
import os 
from collections import defaultdict




# Criando uma função que gera id 

def gerar_id():

    id_ = ""

    numeros = [random.randint(0, 9) for numero in range(0, 5)]

    for numero in numeros:
        id_ += str(numero) 

    return id_ 

print(gerar_id())

# Funções 

# Funções são blocos de código reutilizáveis que são acionados 
# quando chamados 

class Candidato:

    """ Esta classe definine os métodos e os atributos dos objetos Candidato
    que depois serão avaliados por uma função, por meio desta passaram por uma 
    triagem, verificando aptidão para exercimento de um cargo espcífico. """

    def __init__(self, nome: str= None, idade: int= None, cidade: str= "Goiânia", pretencao_salarial: float= 1600, pretencao_vaga: list= []):

        self.__nome = nome if nome != None else ""
        self.__idade = idade if idade != None else ""
        self.__cidade = "" if cidade == None else cidade 
        self.__pretencao_salarial = pretencao_salarial if pretencao_salarial != None else 0 
        self.__pretencao_vaga = [] if pretencao_vaga == None else pretencao_vaga


    # Criando os nossos getters 

    @property 
    def nome(self):
        return self.__nome 

    @property 
    def idade(self):
        return self.__idade 

    @property 
    def cidade(self):
        return self.__cidade 

    @property 
    def pretencao_salarial(self): # Recebemos o próprio objeto como parâmetro e acessa o atributo do objeto 
        return self.__pretencao_salarial 

    @property 
    def pretencao_vaga(self):
        return self.__pretencao_vaga 


    # Criando nossos setters 

    @nome.setter 
    def nome(self, novo_nome: str):
        self.__nome = novo_nome 

    @idade.setter 
    def idade(self, nova_idade: int):
        self.__idade = nova_idade 

    @cidade.setter 
    def cidade(self, nova_cidade: str):
        self.__cidade = nova_cidade 

    @pretencao_salarial.setter
    def pretencao_salarial(self, pretencao_salarial: float):
        self.__pretencao_salarial = novo_pretencao 

    @pretencao_vaga.setter 
    def pretencao_vaga(self, vagas: list):
        self.__pretencao_vaga = vagas 




# Construindo 100 objetos candidatos 





cidades = ["São Paulo",
"Rio de Janeiro",
"Brasília",
"Belo Horizonte",
"Curitiba",
"Manaus",
"Osasco",
"Maricá",
"Porto Alegre",
"Guarulhos"]




cargos = ["Desenvolvedor(a) Full Stack",
"Gerente de Produto (Product Manager)",
"Engenheiro(a) de DevOps",
"Cientista de Dados / Engenheiro de ML",
"Analista de QA (Testes e Qualidade)",
"Designer de UX/UI",
"Engenheiro(a) de Dados",
"Analista de Segurança da Informação",
"Arquiteto(a) de Soluções",
"Engenheiro(a) de Confiabilidade (SRE)"]



def gerar_candidatos(candidatos_gerar_a= 0):

    faker = Faker('pt_BR')


    objetos_candidato = []

    candidatos_gerados, candidatos_gerar = 0, 100  if candidatos_gerar_a == 0 else candidatos_gerar_a
    while candidatos_gerados < candidatos_gerar: 

        nome = faker.name_male()
        idade = random.randint(16, 30)

        random.shuffle(cidades)
        # opcoes = [random.choice(cidades) for _ in range(0, 3)]

        cidade = random.choice(cidades)

        # for cidade in cidades: 

        #     if not cidade in cidades:

        #         cidade_a = cidade 
        #         break   

        pretencao_salarial = random.uniform(1900, 20000)
        pretencao_cargos = random.sample(cargos, 3) # Selecionando uma amostra com três opções cargos.  


        candidato = Candidato(nome, idade, cidade, pretencao_salarial, pretencao_cargos)

        objetos_candidato.append(candidato)

        candidatos_gerados += 1

    return objetos_candidato


candidatos = gerar_candidatos()


# Criando uma função que avalia os candidatos e ver se eles são aptos a exercer uma função especíca 

def gerar_oportunidades():

    oportunidades_abertas = defaultdict(dict)

    # for id_, cargo in enumerate(cargos): 

    for cargo in cargos: 

        id_gerado_lista = random.randint(0, 9)

        salario_a = random.uniform(1900, 10000)

        id_gerado_funcao = gerar_id()
        oportunidades_abertas[id_gerado_funcao]["cargo"] = cargo 
        oportunidades_abertas[id_gerado_funcao]["cidade"] = cidades[id_gerado_lista] 
        oportunidades_abertas[id_gerado_funcao]["salario"] = salario_a 

    return oportunidades_abertas



oportunidades_geradas = gerar_oportunidades()

print(oportunidades_geradas)