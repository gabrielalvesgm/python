import sqlite3

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
