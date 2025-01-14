#Criando uma lista ligada simples utilizando nó

class Node:  #Criando uma classe com nome de nó.
    
 #Função com um método especial __init__ (construtor) que tem self os atributos self (ele mesmo já que não há nenhum valor anterior a ele, e data que vai receber um dado e alocar-lo)
    def __init__(self, data):
        self.data = data #Self (ele mesmo).data recebe o valor de data
        self.proximo = None #None (variável especial) define que não há um próximo nó.
        
class ListaLigada:   #Criando a classe lista ligada.
    def __init__(self):  #método construtor cria uma lista ligada com valor self (ela mesma)
        self.cabeca = None #a variável self.cabeca recebe None pois não há um valor ainda.
        
        
    def inserir_primeiro(self, data): #Criando uma função que define o começo da lista.
        novo_node = Node(data)  #Método construtor cria um novo nó da classe Node.
        novo_node.proximo = self.cabeca #Definindo um novo inicio da lista.
        self.cabeca = novo_node #Atualiza o inicio da lista.
        
    def imprimir_lista(self):  #Função par aexibir a lista
        atual = self.cabeca    #Nova variável define quem é o nó atual (self.cabeca).
        while atual:           #Metodo de repetição enquanto atual for verdadeiro.
            print(atual.data, end=" --> ")
            atual = atual.proximo
        print("None") #Define o fim da lista.
        
    def remover_inicio(self):
        if self.cabeca is None:
            print("Lista vazia.")
            return
        self.cabeca = self.cabeca.proximo #Atualiza a cabeça para o próximo nó.
        
        
#Criando uma lista e testando a lista ligada.
lista = ListaLigada() #Variáveis com um dado
lista.inserir_primeiro(99)
lista.inserir_primeiro(55)    #Variáveis com um dado
lista.inserir_primeiro(40)    #Variáveis com um dado
lista.inserir_primeiro(74)    #Variáveis com um dado

lista.imprimir_lista() #Chamando a função imprimir_lista

lista.remover_inicio()
lista.imprimir_lista()
    
    