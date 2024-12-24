from flask import Flask, jsonify, request  #importando flask como Flask e tradutor JSON
import pandas as pd #importando pandas como pd

app = Flask(__name__)  #inicialização de uma APIs rest

#dicionário dos produtos com chave e valor (key and value)
produtos = [
    {"id": 1, "nome": "Notebook", "preco": 3500},
    {"id": 2, "nome": "Smartphone", "preco": 2000},
    {"id": 3, "nome": "Computador", "preco": 4500},
    {"id": 4, "nome": "Macbook", "preco": 4000},
    {"id": 5, "nome": "SmartWatch", "preco": 1000}
]


#MÉTODO GET (FUNÇÃO LER PRODUTOS)
@app.route('/produtos', methods=['GET'])
def listar_produtos():
    return jsonify(produtos)


#MÉTODO POST (FUNÇÃO ADICIONAR NOVO PRODUTO)
@app.route('/produtos', methods=['POST'])
def adicionar_produtos():
    novo_produto = request.get_json()
    produtos.append(novo_produto)
    return jsonify({"message": "Produto adicionado com sucesso!"}), 201 #HTTP:sucess created.

#MÉTODO PUT (FUNÇÃO ATUALIZAR PRODUTO EXISTENTE [PELO ID])
@app.route('/produtos/<int:produto_id>', methods=['PUT'])
def atualizar_produto(produto_id):
    produto = next((p for p in produtos if p['id'] == produto_id), None)
    if not produto:
        return jsonify({"erro": "Produto não encontrado"}), 404 #HTTP: Not found.
    
    dados = request.get_json()
    produto.update(dados)
    return jsonify(produto), 200 #HTTP: Atualizado com sucesso.


#MÉTODO DELETE (FUNÇÃO REMOVER PRODUTO)
@app.route('/produtos/<int:id>', methods=["DELETE"])
def remover_produto(id):
    produto = next((p for p in produtos if p['id'] == id), None)
    if produto:
        produtos.remove(produto)
        return jsonify({"message": "Produto removido com sucesso"})
    return jsonify({"error!": "Produto não pode ser encontrado."}), 404 #HTTP: Not found.

@app.route('/', methods=['GET'])
def home():
    return jsonify({"mensagem": "Bem-vindo à API de Produtos! Acesse /produtos para listar os produtos."})

if __name__ == '__main__':
    app.run(debug=True)
    
