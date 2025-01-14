import random #IMPORT DA BIBLIOTECA RANDOM

loots = { #DICIONÁRIO LOOTS QUE ATRIBUTIO UMA STRING A CADA NÚMERO DA LISTA
    1: {"nome": "Espada", "descricao": "Uma espada afiada capaz de cortar os inimigos."},
    2: {"nome": "Escudo", "descricao": "Um escudo muito resistente."},
    3: {"nome": "Arco", "descricao": "Um arco preciso e mortal."},
    4: {"nome": "Machado", "descricao": "Um machado pesado e poderoso."},
    5: {"nome": "Lança", "descricao": "Uma lança feroz e pontuda."},
    6: {"nome": "Katana", "descricao": "Uma Katana requintada e super afiada."}
}
def dropar_loot():  #FUNÇÃO DROPAR LOOT .
    numeros = list(loots.keys()) #CRIA UMA LISTA QUE RECEBE AS KEYS DO DICIONÁRIO LOOTS.
    numero_escolhido = random.choice(numeros) #CRIA UMA VARIÁVEL QUE RECEBE UMA RANDOM CHOICE.
    loot = loots[numero_escolhido]
    return loot["nome"], loot["descricao"] # Retorna o nome e a descrição do item

nome, descricao = dropar_loot()
print(f"Você dropou um(a): {nome}\nDescrição: {descricao}")
