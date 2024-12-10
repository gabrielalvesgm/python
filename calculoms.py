class ModaStilos:
    def __init__(self):
        self.cestinha = {}
        self.precos = {"Calça MOM": 35, "Macaquito": 30, "Short Jeans": 40}

    def calcular_juros(self, item, quantidade, metodo_pagamento):
        """Calcula o valor total de um item dependendo da forma de pagamento."""
        preco_base = self.precos[item] * quantidade
        if metodo_pagamento == "Crédito":
            return preco_base + 3 * quantidade
        elif metodo_pagamento == "Débito":
            return preco_base + 2 * quantidade
        elif metodo_pagamento == "Pix":
            return preco_base
        else:
            return 0

    def cestinha_compras(self):
        """Permite ao usuário adicionar itens ao carrinho de compras."""
        print("Olá, seja bem-vindo(a) à Moda Stilos!")
        print("O que deseja comprar hoje?")
        print("Itens disponíveis:")
        for item, preco in self.precos.items():
            print(f"{item} - R${preco}")

        while True:
            item = input("Digite o nome do item que deseja adicionar: ").strip()
            if item not in self.precos:
                print("Item inválido. Tente novamente.")
                continue

            try:
                quantidade = int(input(f"Quantas unidades de {item} deseja adicionar? "))
                if quantidade <= 0:
                    print("A quantidade deve ser maior que 0. Tente novamente.")
                    continue
            except ValueError:
                print("Por favor, insira um número válido.")
                continue

            if item in self.cestinha:
                self.cestinha[item] += quantidade
            else:
                self.cestinha[item] = quantidade

            mais_itens = input("Deseja adicionar mais itens? (S/N): ").strip().upper()
            if mais_itens == "N":
                break

        print("\nItens no seu cestinho:")
        for item, quantidade in self.cestinha.items():
            print(f"{item}: {quantidade} unidades")
        self.escolher_pagamento()

    def escolher_pagamento(self):
        """Permite ao usuário escolher a forma de pagamento para cada item."""
        pagamento = {}
        for item, quantidade in self.cestinha.items():
            while True:
                print(f"\nSelecione o método de pagamento para {quantidade} unidade(s) de {item}:")
                print("1. Pix (sem juros)")
                print("2. Débito (+R$2 por unidade)")
                print("3. Crédito (+R$3 por unidade)")
                metodo = input("Digite o número correspondente ao método de pagamento: ").strip()

                if metodo == "1":
                    pagamento[item] = ("Pix", self.calcular_juros(item, quantidade, "Pix"))
                    break
                elif metodo == "2":
                    pagamento[item] = ("Débito", self.calcular_juros(item, quantidade, "Débito"))
                    break
                elif metodo == "3":
                    pagamento[item] = ("Crédito", self.calcular_juros(item, quantidade, "Crédito"))
                    break
                else:
                    print("Opção inválida. Tente novamente.")

        self.pagar(pagamento)

    def pagar(self, pagamento):
        """Exibe o valor final e encerra a compra."""
        print("\nResumo da compra:")
        total = 0
        for item, (metodo, valor) in pagamento.items():
            print(f"{item}: {metodo} - R${valor:.2f}")
            total += valor

        print(f"\nValor total da compra: R${total:.2f}")
        print("Obrigado por comprar na Moda Stilos! Volte sempre!")


# Instancia a classe e executa o programa
moda_stilos = ModaStilos()
moda_stilos.cestinha_compras()
