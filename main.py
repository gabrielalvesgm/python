#Classe Calculadora que tem dois metodos
class Calculadora:
    
    #metodo para somar dois valores (x e y)
    @staticmethod
    def metodo_soma():
        print(f"Vamos somar!")
        x = int(input(f"Digite o primeiro número para a soma: "))
        y = int(input(f"Digite o segundo número para a soma: "))
        resultadoSoma = x + y
        print(f"O resultado de sua soma é: {resultadoSoma}") 
        
    #metodo para mutiplicar dois valores (x e y)
    @staticmethod
    def metodo_mutiplicar():
        print(f"Vamos mutiplicar!")
        x = float(input(f"Primeiro número para a multiplicação: "))
        y = float(input(f"Segundo número para a multiplicação: "))
        resultadoMultiplicacao = x * y
        print(f"O resultado da sua multiplicação é: {resultadoMultiplicacao:.1f}")
    
    #metodo subtração (subtrai x de y)
    @staticmethod
    def metodo_subtrair():
        print(f"Vamos subtrair")
        x = int(input(f"Primeiro número para a subtração: "))
        y = int(input(f"Segundo número para a subtração: "))
        resultadoSubtracao = x - y
        print(f"O resultado de sua subtração é: {resultadoSubtracao:}")
        
    #metodo para dividir dois valores (x / y)
    @staticmethod
    def metodo_dividir():
        print(f"Vamos dividir")
        x = float(input(f"Digite o primeiro número para a divisão"))
        y = float(input(f"Digite o segundo número para a divisão: "))
        resultadoDivisao = x/y
        print(f"O Resultado da sua divisão é: {resultadoDivisao:.2f}")
    
    #Aqui começa a estrutura if para identificar a função matematica que o usuário irá realizar
    print(f"Qual operação matematica iremos realizar?")
    metodo = input("soma, subtração, mutiplicação ou divisão?")
    
    if metodo == "soma":
            metodo_soma()
        
    elif metodo =="multiplicação":
            metodo_mutiplicar()
        
    elif metodo =="subtração":
            metodo_subtrair()
        
    elif metodo =="divisão":
            metodo_dividir()
        
    else:
            print("Calculo ainda não implementado")