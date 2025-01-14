
# __name__ is the name of the current Python module. The app needs to know where it’s located to set up some paths, and __name__ is a convenient way to tell it that.

# instance_relative_config=True tells the app that configuration files are relative to the instance folder. The instance folder is located outside the flaskr package and can hold local data that shouldn’t be committed to version control, such as configuration secrets and the database file.

# app.config.from_mapping() sets some default configuration that the app will use:

# SECRET_KEY is used by Flask and extensions to keep data safe. It’s set to 'dev' to provide a convenient value during development, but it should be overridden with a random value when deploying.

# DATABASE is the path where the SQLite database file will be saved. It’s under app.instance_path, which is the path that Flask has chosen for the instance folder. You’ll learn more about the database in the next section.

# app.config.from_pyfile() overrides the default configuration with values taken from the config.py file in the instance folder if it exists. For example, when deploying, this can be used to set a real SECRET_KEY.

# test_config can also be passed to the factory, and will be used instead of the instance configuration. This is so the tests you’ll write later in the tutorial can be configured independently of any development values you have configured.

# os.makedirs() ensures that app.instance_path exists. Flask doesn’t create the instance folder automatically, but it needs to be created because your project will create the SQLite database file there.

# @app.route() creates a simple route so you can see the application working before getting into the rest of the tutorial. It creates a connection between the URL /hello and a function that returns a response, the string 'Hello, World!' in this case.

from flask import Flask, request, jsonify
import os



app = Flask(__name__)



produtos = []



@app.route('/')
def home():
    return "Bem-vindo à api de Catálogo de Produtos!"



if __name__ == "__main__":
    app.run(debug=True)
    
    
@app.route('/produtos', methods=['GET'])
def listar_produtos():
    return jsonify(produtos)


@app.route ('/produtos', methods=['POST'])

def criar_produtos():
    dados = request.get.json()
    
# Verifica se todos os dados necessários estão presentes

    if not dados.get('nome') or not dados.get('preco') or not dados.get('categoria'):
        return jsonify({'erro': 'Faltam dados obrigatórios!'}), 400

    novo_produto = {
    'id' : len(produtos) + 1,
    'nome' : dados['nome'],
    'preco' : dados['preco'],
    'categoria' : dados['categoria'],
    'descricao' : dados.get('descricao', '') #Descrição é opicional    
}

    produtos.append(novo_produto)

    return jsonify(novo_produto), 201

def buscar_produto(id):
    produto = next((p for p in produtos if p['id'] == id), None)
    
    if produto is None:
        return jsonify({'erro': "Produto não encontrado"}), 404
    return jsonify(produto)


#ENDPOINT PARA ATUALIZAR O PRODUTO!
@app.route('/produtos/<int:id>', methods=['PUT'])
def atualizar_produto(id):
    dados = request.get_json()
    
    produto = next((p for p in produtos if p['id'] == id),   None)
    
    if produto is None:
        return jsonify({'erro': 'Produto não encontrado!'}), 404
    
    
    produto['nome'] = dados.get('nome', produto['nome'])
    produto['preco'] = dados.get('preco', produto['preco'])
    produto['categoria'] = dados.get('categoria', produto['categoria'])
    produto['descricao'] = dados.get('descricao', produto['descricao'])
    
    return jsonify

#ENDPOINT PARA DELETAR UM PRODUTO!
@app.route('/produtos/<int:id>', methods=['DELETE'])
def deletar_produto(id):
    global produtos
    produtos = [p for p in produtos if p['id'] != id]
    
    return jsonify({'mensagem': 'Produto deletado com sucesso!'})
    