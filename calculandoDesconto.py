def calcular_descontos():
    print("Vamos calcular o seu desconto")
    try:
        valor = float(input("Digite aqui o preço do produto que deseja calcular o desconto: "))
        print(f"O preço do produto é R${valor:.2f}, agora digite o valor do desconto: ")
        desconto = float(input("o valor do desconto é: "))
    
        resultado = valor * desconto / 100
        print(f"O Seu produto de: {valor:.2f}R$ terá um desconto de: {desconto:.1f}%"
              f" e passará de: R${valor:.2f}, para: R${valor - resultado}R$. Aproveite a oferta.")
    except ValueError:
        print("Digite o valor e desconto válido")
calcular_descontos()