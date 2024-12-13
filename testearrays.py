#Arrays em Python!


#Importando a biblioteca ARRAYS
import array           


#criando a variável numeros que recebe o array de inteiros ('i')
elementos = array.array('i', [21, 17, 41, 33, 52, 56, 7, 36, 77])


#Criando a função encontrar_maior() que recebe o parâmetro arr que recebe um array
def encontrar_maior(arr):
    maior = arr[0]    #Variável  que recebe o array 'arr'[0] de indice 0 (21)
    for numeros in arr:      #Chamada do laço for in arr - percorre todo o array de 0 ao fim
        if numeros > maior:  #Chamada da estrutura condicional if -verifica (numeros > maior)
            maior = numeros  #Se o próximo número a cada iteração for maior recebe maior
    return maior  #Após numeros percorrer todo o array, retorna o maior número.

maior_valor = encontrar_maior(elementos)
print(f"O maior número do array é: {maior_valor}")
    