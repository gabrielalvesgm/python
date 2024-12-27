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

#:-::-::-::-::-:Funções de auxílio:-::-::-::-::-:

#Função que evita dois produtos com o mesmo nome.
#A função implementa a lógica de que sempre que um nome já existente for adicionado no código ele receberá um (+1) no final.

def gerar_nome_unico(nome, conn):
    cur = conn.cursor()
    cur.execute("SELECT nome FROM produtos WHERE nome LIKE ?", (f"{nome}%",))
    nomes_existentes = [row[0] for row in cur.fetchall()]
    
    if nome not in nomes_existentes:
        return nome
    
    contador = 2
    while True:
        novo_nome = f"{nome} ({contador})"
        if novo_nome not in nomes_existentes:
            return novo_nome
        contador += 1


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
    
    # Função auxiliar para evitar duplicatas
    nome_unico = gerar_nome_unico(novo_produto["nome"], conn)
     
    cur = conn.cursor()
    cur.execute("INSERT INTO produtos (nome, descricao) VALUES (?, ?)",
                (nome_unico, novo_produto.get("descricao", None))) 
    conn.commit()
    conn.close()
    return jsonify({"message": f"Produto '{nome_unico}' criado com sucesso!"}), 201

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

    