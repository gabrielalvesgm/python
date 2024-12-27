import sqlite3
from flask import Flask, request, jsonify

conn = sqlite3.connect("dbprojetolojavrt.db") #database
cur = conn.cursor()

#Tabela da database
cur.execute('''
CREATE TABLE IF NOT EXISTS produtos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    descricao TEXT
);           
''')
conn.commit() #commit
conn.close() #close

def get_db_connection():  #conectando a database ao server
    conn = sqlite3.connect("dbprojetolojavrt.db")
    conn.row_factory = sqlite3.Row
    return conn

app = Flask(__name__) #Inicializando o app Flask

#:-::-::-::-::-:Operações CRUD:-::-::-::-::-:

@app.route('/')
def home():
    return jsonify({"mensagem": "Bem-vindo à API da Loja Virtual!"})

@app.route('/produtos', methods=['GET'])
def obter_produtos():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM produtos;")
    produtos = cur.fetchall()
    conn.close()
    return jsonify([dict(produto) for produto in produtos])


@app.route('/produtos', methods=['POST'])
def criar_produto():
    novo_produto = request.get_json()
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO produtos (nome, descricao) VALUES (?, ?)",
                (novo_produto["nome"], novo_produto.get("descricao", None)))
    conn.commit()
    conn.close()
    return jsonify({"message": "Produto criado com sucesso!"}), 201

@app.route('/produtos', methods=["PUT"])
def atualizar_produto(id):
    produto_atualizado = request.get_json()
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("UPDATE produtos SET nome = ?, descicao = ? WHERE id = ?",
                (produto_atualizado["nome"], produto_atualizado.get("descricao", None), id))
    conn.commit()
    conn.close()
    return jsonify({"message": "Produto atualizado com sucesso!"})

@app.route('/produtos/<int:id>', methods=["DELETE"])
def deletar_produto(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM produtos WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return jsonify({"message": "Produto deletado com sucesso!"})


if __name__ == "__main__":
    app.run(debug=True)

    