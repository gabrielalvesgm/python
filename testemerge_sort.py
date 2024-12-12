#TESTANDO O MÉTODO MERGE SORT

def merge_sort(lista):
    if len(lista) <= 1:
        return lista
    
    meio = len(lista) //2
    esquerda = lista[:meio]
    direita = lista[meio:]
    
    esquerda = merge_sort(esquerda)
    direita = merge_sort(direita)
    
    return merge(esquerda, direita)

def merge(esquerda, direita):
    lista_ordenada = []
    i = j = 0
    
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] < direita[j]:
            lista_ordenada.append(esquerda[i])
            i += 1
        else:
            lista_ordenada.append(direita[j])
            j += 1
            
    lista_ordenada.extend(esquerda[i:])
    lista_ordenada.extend(direita[j:])
    
    return lista_ordenada

elementos = [31, 27, 84, 11, 15, 17, 63, 43, 25, 76, 93]
resultado = merge_sort(elementos)
print("Lista ordenada merge_sort:", resultado)
