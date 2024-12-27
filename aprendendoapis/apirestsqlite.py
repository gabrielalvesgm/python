import sqlite3
from flask import Flask, request, jsonify




conn = sqlite3.connect("sqliteexemplo.db") #Conectando com a database
cur = conn.cursor()

#Criando uma tabela chamada usuários:
cur.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE
);
''')
conn.commit()
conn.close

#Função que configura o database
def get_db_connection():
    conn = sqlite3.connect('sqliteexemplo.db') #database que foi criada sendo conectada.
    conn.row_factory = sqlite3.Row #Retornar os resultados como dicionários.
    return conn

#Criando e inicializando o aplicativo com flask
app = Flask(__name__)

@app.route('usuarios', methods = ['GET']) #Método GET do aplicativo.
def obter_usuarios():
    conn = get_db_connection()
    cur = conn.cursor
    cur.execute('SELECT * FROM usuarios;')
    usuarios = cur.fetchall()
    conn.close()
    return jsonify([dict(usuario) for usuario in usuarios])

@app.route('/usuarios', methods=['POST']) #Método POST do aplicativo.
def criar_usuario():
    novo_usuario = request.get_json()
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO usuarios (nome, email) VALUES (?, ?)',
                (novo_usuario['nome'], novo_usuario['email']))
    conn.commit()
    conn.close()
    return jsonify({'mensagem': "Usuário criado com sucesso!"})

@app.route('/usuarios/<int:id>', methods=['PUT']) #Método put (em /usuarios/<int:id>)
def atualizar_usuario(id):
    usuario_atualizado = request.get_json()
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('UPTADE usuarios SET nome = ?, email = ? WHERE id = ?',
                (usuario_atualizado['nome'], usuario_atualizado['email'], id))
    conn.commit()
    conn.close()
    return jsonify({'mensagem': "Usuário atualizado com sucesso!"})


@app.route('/usuarios/<int:id>', methods=['DELETE'])
def deletar_usuario(id):
    conn = get_db_connection
    cur = conn.cursor()
    cur.execute('DELETE FROM usuarios WHERE id = ?', (id))
    conn.commit()
    conn.close()
    return jsonify({"mensagem": "Usuário deletado com sucesso."})

#Como executar o servidor:

if __name__ == '__main__':
    app.run(debug=True)
    
    
