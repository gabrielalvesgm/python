#TESTANDO O MÉTODO QUICKSORT NO PYTHON.


def quick_sort(lista): #Função quick_sort que recebe uma lista.
    if len(lista) <= 1: #Se tamanho da lista é menor ou igual a um-
        return lista #retorna a lista pois não há oque ordenar.

    pivot = lista[-1] #pivot será o último elemento da lista.
    
    menores = [] #lista ''menores'' 
    maiores = [] #lista ''maiores'' 
    
    for item in lista[:-1]: #iterando na lista item do primeiro ao último elemento (-pivot)
        if item <= pivot: #Se item é menor ou igual a pivot
            menores.append(item) #lista menores armazena (item)
        else: #senão
            maiores.append(item) #lista maiores armazena (item)
            
    # Retorna a concatenação de:
    # 1. A lista ordenada de menores (recursivamente ordenada).
    # 2. O pivô como um elemento central.
    # 3. A lista ordenada de maiores (recursivamente ordenada).
    return quick_sort(menores) + [pivot] + quick_sort(maiores)


numeros = [32, 11, 43, 66, 45, 78, 91, 65, 35, 15, 57] #elementos a serem ordenados:

resultado = quick_sort(numeros) #chamado da função + armazenamento do resultado.

print("Lista ordenada :", resultado) #mostra lista ordenada.
