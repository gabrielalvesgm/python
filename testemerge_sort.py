# TESTANDO O MÉTODO MERGE SORT

def merge_sort(lista):
    if len(lista) <= 1:  # Se a lista tiver 1 ou nenhum elemento, já está ordenada.
        return lista
    
    meio = len(lista) // 2  #Divide a lista ao meio.
    esquerda = lista[:meio]  # Parte esquerda da lista, do início até o meio.
    direita = lista[meio:]  #Parte direita da lista, do meio até o final.
    
    # Aplica recursivamente o merge_sort na esquerda e na direita.
    esquerda = merge_sort(esquerda)
    direita = merge_sort(direita)
    
    #Combina as partes ordenadas e retorna a lista ordenada.
    return merge(esquerda, direita)

def merge(esquerda, direita): 
    lista_ordenada = []  # Lista que armazena os elementos ordenados.
    i = j = 0  # Índices para percorrer as listas esquerda e direita.
    
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] < direita[j]:  # Se o elemento da esquerda for menor.
            lista_ordenada.append(esquerda[i])  #append a lista ordenada
            i += 1  #verificando e movendo o índice para esquerda
        else:  #caso contrário, o elemento da direita é menor ou igual.
            lista_ordenada.append(direita[j])  # append a lista ordenada
            j += 1  #verificando e movendo o índice para a direita
    
    lista_ordenada.extend(esquerda[i:])  #Junta a esquerda.
    lista_ordenada.extend(direita[j:])  #Junta a direita.
    
    return lista_ordenada #Retorna a lista ordenada.

elementos = [31, 27, 84, 11, 15, 17, 63, 43, 25, 76, 93]  #Elementos para ordenar.
resultado = merge_sort(elementos)  #Chamando a função.
print("Lista ordenada merge_sort:", resultado)  #Print da lista ordenada.