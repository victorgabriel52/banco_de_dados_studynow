import sqlite3
import os

def banco():
    pasta_atual = os.path.dirname(os.path.abspath(__file__))
    caminho = os.path.join(pasta_atual, "banco_dados.db")
    return sqlite3.connect(caminho)

def criar_tabela():
    con = banco()
    cur = con.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cpf TEXT UNIQUE NOT NULL,
        senha TEXT NOT NULL
    )
    """)
    con.commit()
    con.close()


