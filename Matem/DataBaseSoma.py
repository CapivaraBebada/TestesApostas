# Script: bd_soma.py
import sqlite3

# Conectando ao banco de dados
conn = sqlite3.connect('Soma.db')
cursor = conn.cursor()

# Criando a tabela, se não existir
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Somatorio (
        Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        Numero1 REAL NOT NULL,
        Numero2 REAL NOT NULL,
        Resultado REAL NOT NULL
);
""")

conn.commit()

print('Banco de dados e tabela criados com sucesso.')
