#TESTANDO O BUBBLE SORT!

def bubble_sort(lista): #Criando a função bubble_sort que recebe uma lista.
    n = len(lista) #Variável n recebe tamanho da lista.
    for i in range(n - 1): #i percorre na range lista -1 (ultimo elemento por indice)
        for j in range(n - 1 - i): #J percorre até o penultimo elemento (já que i é o último.)
            if lista[j] > lista[j + 1]: #if compara o elemento atual e próximo na lista.
                lista[j], lista[j + 1] = lista[j + 1], lista[j] #Se o elemento atual for maior que o próximo, trocam de posições.
    return lista #retorna a lista ordenada.

numeros = [88, 14, 85, 91, 63, 65, 86, 16, 19, 21, 72, 33, 10] #lista a ser ordenada.

resultado = bubble_sort(numeros) #Chama a função bubble_sort com a lista e armazena o resultado.

print("Lista ordenada:", resultado) #Mostra a lista ordenada.