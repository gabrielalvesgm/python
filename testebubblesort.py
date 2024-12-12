#AQUI IREMOS CRIAR NOSSA PRIMEIRA ORDENAÇÃO BUBBLESORT EM PYTHON.

#Passo a passo:
#Primeiro cria-se uma função (def) para encapsular o Bubble Sort e tornalo reutilizável.
#Segundo cria-se um loop (for) para iterar sobre uma sequência (lista) ou em intervalos.
    #O Bubble sorte irá comparar pares com o for.
#Terceiro cria-se um (range) que irá criar uma sequência de números dentro de um intervalo.
    #É necessário para controlar o número de iterações no loop.
#Quarto Cria-se uma (len) que retorna o tamanho (quantidade de elementos)de 1 lista ou coleção
    #len irá calcular o número de elementos na lista e definir os limites.
#Cria-se uma condição (if) que irá definir elementos como verdadeiro ou falso.
    #Verifica se os dois elementos estão fora de ordem e se precisam ser trocados de lugar.
#Método de desempacotamento/troca de valores (a, b = b, a)
    #Troca os valores de duas variáveis de forma conscisa e reorganiza os elementos na lista.
#Fim da função com (return) sai da função e retorna o (valor)
    #Retornará a lista ordenada após o fim do bubble sort.


lista = numeros = [88, 14, 85, 91, 63, 65, 86, 16, 19, 21, 72, 33, 10]

def bubble_sort(lista):
    n = len(lista)
    for i in range(n - 1):
        for j in range(n -1 - i):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]   #desenpacotamento
    return lista
bubble_sort(lista)