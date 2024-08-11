import sqlite3
    # Conectando ao banco de dados
conn = sqlite3.connect('TesteAposta.db')
cursor = conn.cursor()

# TABELA GERAL
cursor.execute(""" 
    CREATE TABLE IF NOT EXISTS AnaliseTeste (
        Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        Data INTEGER NOT NULL,
        Competicao TEXT NOT NULL,
        Casa TEXT NOT NULL,
        Fora TEXT NOT NULL,
        Mercado TEXT NOT NULL,
        Odd REAL NOT NULL,
        Unidade REAL NOT NULL,
        L_P REAL NOT NULL,
        Montante REAL NOT NULL
    );
""") 
print('Conectado ao Bnaco de dados 1')


cursor.execute("""
    CREATE TABLE IF NOT EXISTS InicioLucroTotal(
        Inicio REAL NOT NULL,
        Lucro REAL NOT NULL,
        Total REAL NOT NULL
    );
""")
print('Conectado ao Banco de Dados 2')


cursor.execute(""" 
    CREATE TABLE IF NOT EXISTS GreenRed (
        Green REAL NOT NULL,
        Red REAL NOT NULL
    );
""")
print('Conectado ao banco de dados 3')


conn.commit()
