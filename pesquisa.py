import sqlite3
import pandas as pd

con = sqlite3.connect('agenda.db')
cur = con.cursor()

resultado = cur.execute("select * from CONTATO")

nome = []
endereco = []

for linha in resultado.fetchall():
    print(linha)
    print(type(linha))
    nome.append(pd.Series(linha[0]))

print(pd.Series(nome))

dados = pd.DataFrame({'Nomes':nome, 'Enderecos': endereco})

print(dados)