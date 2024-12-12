#TESTANDO O MÉTODO QUICKSORT NO PYTHON.


numeros = [32, 11, 43, 66, 45, 78, 91, 65, 35, 15, 57]

def quick_sort(lista):
    if len(lista) <= 1:
        return lista

    pivot = lista[-1]
    
    menores = []
    maiores = []
    
    for item in lista[:-1]:
        if item <= pivot:
            menores.append(item)
        else:
            maiores.append(item)
            
    return quick_sort(menores) + [pivot] + quick_sort(maiores)

resultado = quick_sort(numeros)
print("Lista ordenada :", resultado)
