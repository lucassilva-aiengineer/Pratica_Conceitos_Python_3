# Geradores 
# Os geradores são algo como um lista temporária, uma lista que contém itens 
# temporários. 

def geradores(alvo):

    gera = 0
    while gera < alvo: 

        yield gera 

        gera += 1

    return gera 


meus_geradores = geradores(10)

# print(list(meus_geradores))
# print(list(meus_geradores))

for numero in meus_geradores: 
    print(numero)